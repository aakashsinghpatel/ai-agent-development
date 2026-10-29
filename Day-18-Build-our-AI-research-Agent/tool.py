import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, parse_qs
from ollama import chat
import json
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

# pip install tavily-python
# for replacing duckduckgo
MODEL = "qwen3:1.7b"

research_notes = []

def search_web(query, max_results=5):
    """
        Search the web using DuckDuckGo.
    
        Args:
            query: Search query.
            max_results: Maximum number of results.
    
        Returns:
            A list of search results.
    """
    
    try:
        """ In duckduckgo getting authentication issue as captha verification
         while call form python so alternatively use tavily """
        # headers = {
        #     "User-Agent": (
        #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        #         "AppleWebKit/537.36 (KHTML, like Gecko) "
        #         "Chrome/130.0.0.0 Safari/537.36"
        #     ),
        #         "Accept-Language": "en-US,en;q=0.9",
        #     }
        # respose = requests.get("https://html.duckduckgo.com/html/", 
        #                        params={"q": query}, 
        #                        headers = {"User-Agent": "Mozilla/5.0"}, timeout=20)
        # respose.raise_for_status()

        # soup =  bs(respose.text, "html.parser")
        results =[]

        client = TavilyClient(os.getenv("TAVILY_API_KEY"))
        response = client.search(
            query=query,
            search_depth="advanced"
        )

        # print(len(soup.select(".results")))
        # for result in soup.select(".result")[:max_results]:
        #     title = result.select_one(".result__title")
        #     url = result.select_one(".result__a")
        #     snippet =result.select_one(".result__snippet")

        #     if not url:
        #         continue
        res = response.get('results', [])
        if len(res) > 0 :
            for result in res[:int(max_results)]:
                title = result.get("title","")
                url = result.get("url", "")
                snippet = result.get("content", "")

                if not url:
                    continue

                results.append({ "title": title,"url": url,"snippet": snippet})
        return results
    except Exception as e:
        print(e)


def read_webpage(url):
    """
    Download a webpage and extract its text.
    Args:
        url: Webpage URL.
    Returns:
        Extracted webpage text.
    """    
    try:
        if url.startswith("//"):
                url = "https:" + url
        # Extract the real URL from 
        #  DuckDuckGo redirect URL
        parsed_url = urlparse(url)
        if "duckduckgo.com" in parsed_url.netloc:
                params = parse_qs(parsed_url.query)
                if "uddg" in params:
                    url = params["uddg"][0]
        response = requests.get(url,headers={
                            "User-Agent": "Mozilla/5.0"
                        },timeout=20)
        response.raise_for_status()
        
        soup = bs(response.text,"html.parser")
        
        for element in soup(["script", "style", "noscript"]):
            element.decompose()
        
        text = soup.get_text("\n",strip=True)
        
        return text[:12000]
    
    except Exception as e:
        print(e)


def add_research_note(source, finding, evidence):
    """
    Store an important research finding.

    IMPORTANT:
    This tool accepts exactly three arguments:

    source: The URL or name of the source.

    finding:The specific claim or conclusion extracted from the source.

    evidence:The text or information from the source that supports the finding.

    Do not use title or summary.
    
    Returns:
        Confirmation message.
    """

    research_notes.append({
        "source": source,
        "finding": finding,
        "evidence": evidence,
        "verified": False
    })

    return {
        "status": "stored",
        "finding": finding
    }


def get_research_notes():
    """
    Return all research notes collected so far.
    """

    return [
        note.copy()
        for note in research_notes
    ]

def mark_note_verified(source, finding):
    """
    Mark a matching research note as verified.
    """
    for note in research_notes:
        if (note["source"] == source and note["finding"] == finding):
            note["verified"] = True
            return {
                "status": "verified",
                "finding": finding
            }

    return {
        "status": "not_found",
        "finding": finding
    }

def verify_finding(source,finding,evidence):
    """
    Check whether evidence supports a finding.
    """
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an evidence verification assistant. "
                    "Determine whether the supplied evidence "
                    "supports the supplied finding. "
                    "Return JSON with exactly two fields: "
                    "supported and explanation. "
                    "supported must be true or false."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Source:\n{source}\n\n"
                    f"Finding:\n{finding}\n\n"
                    f"Evidence:\n{evidence}"
                )
            }
        ],
        format="json"
    )

    result = json.loads(
        response.message.content
    )

    if result["supported"]:
        mark_note_verified(source,finding)

    return result


def get_verified_research_notes():
    """
    Return only verified research notes.
    """
    return [note.copy() for note in research_notes if note.get("verified", False)]
