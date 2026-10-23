

def create_chunks(text , source, chunk_size=200, overlap=20):
    """ Fixed chunking This method create the chunks(word based chunks) of pass document text
        chunk_size: text content in each chunk, 
        overlaop: repeached characted lenght in each adjacent chunk: to keep context between chunk 
        source: name of document for which content is gettign chunked 
         
         Chunking Type: FIxed sie chunking, Paraa chunking, Heading chunkig
         """
    words = text.split()
    
    chunks = []
    start = 0
    chunk_step = 0

    while start < len(words):
        end = start + chunk_size
        chunk_text = "".join(words[start:end])
        chunks.append({
            "text": chunk_text, 
            "source": source , 
            "chunk_id": f"chunk-{chunk_step}"
            })
        chunk_step+=1
        start += chunk_size-overlap
    return chunks