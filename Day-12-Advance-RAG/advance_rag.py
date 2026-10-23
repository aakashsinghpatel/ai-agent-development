from chunker import create_chunks
from embedding import (embed_chunks,create_embedding)

from chroma_store import (add_chunks, search_chunk as chroma_search)

from retriever import keyword_score
from reranker import rerank


def build_rag(text, source):
    """ This is to create RAG knowledge base 
     store document chunks into chromaDB
     """
    chunks = create_chunks(text,source=source,chunk_size=200,overlap=50)

    embedded_chunks = embed_chunks(chunks)

    add_chunks(embedded_chunks)
    return embedded_chunks


def retrieve(query,top_k=5, sementic_weight=.6, keyword_weight=.3):
    """ Retrive best candidates from chromaDB DB late based on hybrid search """
    query_embedding = create_embedding(query)

    """ If this search not ther then manually we have to loop through each chunk of document and hget 
     semantic and keywork score: as done on retriver.py """
    semantic_results = chroma_search(query_embedding,top_k=top_k)
    candidates = []
    documents = (semantic_results["documents"][0])
    metadatas = (semantic_results["metadatas"][0])
    """ It show how far the chunk meaning wise away from query """
    distances = (semantic_results["distances"][0])
    for i in range(len(documents)):
        text = documents[i]
        metadata = metadatas[i]
        distance = distances[i]
        semantic = 1 / (1 + distance)
        keyword = keyword_score(query,text)

        combined = (sementic_weight * semantic+ keyword_weight* keyword)
        candidates.append({
            "text": text,
            "source": metadata["source"],
            "chunk_id": metadata["chunk_id"],
            "semantic_score": semantic,
            "keyword_score": keyword,
            "combined_score": combined
        })

    candidates.sort(
        key=lambda item:
        item["combined_score"],
        reverse=True
    )

    candidates = candidates[:top_k]
    print(                "\nRetrieved Sources Candidates:"
            )
    
    for candidate in candidates:
        print(f"- "f"{candidate['source']} "f"(chunk "f"{candidate['chunk_id']})")
    
    return rerank(query,candidates,top_k=3)
