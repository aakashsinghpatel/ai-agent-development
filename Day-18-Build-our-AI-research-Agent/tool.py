import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse, parse_qs


def search_web(query, MAX_RESULT=5):
    """ This tool will serach the web for the query with DuckDuckGO.
     arguments: query
      Result: List of top max element result
        [{title, URL}] """
    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/130.0.0.0 Safari/537.36"
    ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        respose = requests.get("https://html.duckduckgo.com/html/", 
                               params={"q": query}, 
                               headers = {"User-Agent": "Mozilla/5.0"}, timeout=20)
        respose.raise_for_status()

        soup =  bs(respose.text, "html.parser")
        print(soup)
        results =[]
        print(len(soup.select(".results")))
        for result in soup.select(".result")[:MAX_RESULT]:
            title = result.select_one(".result__title")
            url = result.select_one(".result__a")
            snippet =result.select_one(".result__snippet")

            if not url:
                continue

            results.append({ "title": (title.get_text(" ",strip=True) if title else ""),
                        "url": url.get("href",""),
                        "snippet": (snippet.get_text(" ",strip=True) if snippet else ""
                        )})
        
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