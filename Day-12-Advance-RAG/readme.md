## Advance RAG
Tii now, it was basic RAG
Document -> Embedding -> Similarity Score -> Relevant document
    here, embeding checking is done manually to find similarity score for each chunk of doc to query embedding. it there is 1000,000 chunk then manually it will be very complicated hnce 
Advanced RAG: Extract only that chuck which contain answer rather reading whole document.

Suppose document has 20 pages.
User ask the question?
Then we dont want to provide whole 20 page document to LLM to genrate response.
we want just provide part of  document that enough to anser the question.

Hence, break the document into chunks, create embedding of chunks and later return on relevant chunk. (Piece of document either param,page etc)

#### chunking:
    Process of convering document into small  part
    document -> [chunk1, chunk2 ......]
    user request -- retrieve -> chunk (previously whock doc)

    We should not split document Randomly
    Random chunking can destroy the information, as saperate the important information and result in losing context.

    There for to maintain the context overlaping is done.

    Chunking type:
        Fixed Lenght (character or word)
        Paragraph based chunking
        Heading based chunking

    With chunking with add important featuer calling Overlap. it is repeatavive part in two adjacent chunk that keep the context and keep the information.

    Why ovelap:
        * As information near boundary of chunk appear in both chunk
        * This improve the context while retrieving the chunk help to maintain context
        * But overlap should not be execessive
            ex: chunk size: 100,, over lap=90
        This will create problems:
            -> Create enoromous duplication
            -> increase storage for chunk, embedding 
        So overlapping should be managable not excessive.

### Building document chunking startegy with methdata:
    > chunke.py
        create_chunk(text , source, chunk_size=200, overlap=20) -> [chunk]
            text: the content of doc (name)
            sorce; file name
        
        each chunk has : text, source, chunk_id
        here source and chunk_id is metadata (data about chunk)

        we also need embedding so that we can do sementic serch on chunk.

### Generate enbedding of chunk:
    > embedding.py
        embed_chunks(chunks: chunk): embeded_chunk[{}]

            embedded chunk: {text, source, chunk_id, embedding}

### Build semantic search for intelligen retriver:
    query -> embeding of query -> compare it wih each document chunk embedding (vector) -> get the relevant chunk <Candidate> -> Similarity -> top results

    The top chunks that retieved after sementic search that relvant to question are know as
    'candidate'.
    >retiver.py 
        > cosine _similarity(v1, v2)
        > sementic_search(query, chunks, top_k)
    
    Sementic Serch: 
        this is very good  meaning, even for the question haveing differnt word but semanticaly same.

        But there are question where this nowwork well: "What doed 'generate_password does'?
    here to answer exact word need to be match, so here  keyword serch or exact word based searching wiil be efficiend.

    semantic search                             Keyword search
    ------------------------------------------------------------------------
    -> Good for meaning                         -> Exact word/item
    -> COncept                                  -> Identifier
    -> Peraphrashing                            -> name
    -> natural language                         -> rare technical words.
    * for this all case need semantic searc     * For all this need exact word match search

    > keyword_score(query, text):
        query: User query
        text: the chunk text
        Both convert to set of word and fine how many word of qury available into chunk
        accordinly each achunk adde with keyword score.
### Bulding Hybrid search:
    combine foth sementic and Keyword search.

    queery -->  Sementic serch (emvedding)     -> Sementic score -
            |-> Keyword search (word exitance) -> keyword score  -| combine Score -> top Result

        
    > hybris_search(query, chunks, top_k<used for candidates>, keyword_weight, semenatic weight):
        * find keyword, semnatic and combined<hybrid> score for each chunk
            combined_score = (keywordscore* keyword weight+ sementic score * semetic weight)
        result :[{text, chunk_id, source, semantic_score, keyword_score, combined_score }]
        * sort tht list nased on combined score
        * return top_k from result
### Undersatnd re-ranknig in finding most relevent result:
    Suppoer hybrid serch returm 5 relvat chunk or candidant.
    But how we know which on is not relevant.
    They are resenable relevan tbut not perfact ranked.
    Findig the candindate whoch are most relvent with rellevancy score (rank)

    Flow:
        Query -> Hybrid search-> condidates -> Re-ranker -> Best result -> LLM -> answer

        This process of getting best result with adding rank based on most relevancy from condidate is re ranking.
    Idea:
        retieval (Search) find candidate
        Reranking  find best releveant resuls.
    
    > reranke.py:
        rerank(query, candidates, top_k):
            * use LLM/prompt to give rank to each candidate based on how each best for answer query from range.
            * accordingly top_k best ranked result will be return

    Issue: In ranker, we can see for each canndidate rank it getting evaluated by LLM call.
    As this make systemr very slow and inefficient. (We tried this for undertanding the working)

    But for production application, specific LLM model will be used for RE-Ranking.

### Build  vector store FAISS and chromaDB:
    Till now, for semenatic search to get the top_k candidate we are manually comparing embedding of query wirh each chunk and accordingly top_k are calculatng.

    But if there is huge document and huge chunking 100,000 then manuallly doing this whole make inefficient.
    Also wherever program start each time chuning, embedding and storing of doc need to be done which is also in efiifcient.

    To solve this.: Vecore DB: This doed not replace embedding but it come to easy the process or sementic search 
    Her also embedding need to be done.

    * FAISS: Primary gives  vector indexing/search.
    * chromaDB: Give complte development abstraction ro developed
      > pip install chromadb
        It help to store whole doc embedding , metada with searching capability on embedding to get candidates. (Replace of flow to cget candidate based on semantic search partially)

        With this document/chunk embedding can be store on persiatant databases, so that each time no need to create chunk and embeeding
        also provide search capabilities on vectors 
        * chromaDB stre embedding/vector it not replacemet for embedding.
    It store:
        document-text, embedding, metadata, collection,persistant, vector search

        chroma DB maintain
        ID
        -> Document
        -> embedding
        -> Metadata
        Chroma DB jsu store and retieve it is not related to embedding geeration.
    > chroma_store.py
        pip install chromadb
        * add_chunks(chunks:[{text, embedding, source, chunk_id}]):
            collection.upsert(documents, embedding, ids, metadata)

            upsert: will add new data to collection and also udate the data based on id
            ID is unique for collection to store dataor retrive data.
            ID distinuguies between tow document. embedding
### Build sementic serch with chromaDB
    As we have ise persistnt client therefor DB/dbfile is om local
    > chroma_store.py
        serch(query_embedding, top_l):
            collection.query(query_embeeding=[query_embedding], nresult=top_k)

        This will retuen top_k relevant candidate based on embedding of useer query.
        The result doucment, metadata, distances are nestedarray as chroma DB can ceecure multple query at a time.

        distance: it show how far the return embedding is from useer query embedding.

        this will be used for calculating sementic score (show how querya nd chunk relatable/near)            

### Evaluating & Improving RAG Retrival quality:
    we can improve the retrivel by metadata filter.
        like 
        collection.query(query_embeeing=[embeddimh], n_result=topk,
            where={source="filename"})

        This adding filter by methdata know as metadata filter this improve rerival.

    # Embedding generation does not mean retrival will be good, retrival alsl depend on
        1. Chunk size 2. Overlap 3. Embedding model 4. Serch technique
        5. Ranking 6. query qulity

        Byt changeing this based on experimention retrival can be improve and better.

    > evalution.py:
        evaluate_retrieval():
        This evalute retrival bases on chunk availabiltu check inthe candidates.
        as per this for a query a perticual chunk must be there in candidat echunk.
        Hence till is check her.

        In productio syster, a large evalutio dataset is created first to measure thr RAG retieval.
    It work on flow:
        
        Build  -> Measure -> Improve -> Measure

        This hekp to improve the retrival by adhustin , chunksize, overlap, top_k, al othere.

### Build complte advance RAG:
   the workflow wiil be:
    
    Document -> chunking -> Overlap+ metadata -> embedding -> 
        chromaDB -> Vecor search -> Hybrid search(Sementic score, keyword score) -> candidates
        -> Reranked -> Top results -> Abswer genratot (LLM) -> Answer

    > advance_rag.py:
        build_rag(text, source):
            * chunking
            * embedding of chunks
            * store in chromaDB
        retrive(userQuery, top_k,sementic_score, keyword_score):
            * user enbeeding
            * candidate form chromaDB
            * do hybrid serch baed on DB output (distase) and keyword score(usee query, document of DB) calculation
            * find top_k high score candidate.
            * return reran result: top ranked (most relveant) result
### Build final answer
    >generator.py
        create natiral anseerwith LLM and propr wih quser query and retrival resilt (rerank result)
        use rerank result as context

### Run thr advance rag
 >runner.py
  1. build rag knowlege base i.e store chunks into chromaDB : build_rag
  2. take user query
  3. retieve result with user qeuey from RAG
  4. generate answer with using query and result as context
  5. show as answer

###  Review  :: 
    * Use same embediign model for embedding of query and chunking.
    * metadate to retiever let it know from where info came
    * Over lap preserve context
    * sementci serch not always successful it based on user query whcih search will be good
    * Hybrid serch (Seentic serch + keyword search)
    * FAIIS: vector indexing technique
    * ChromaDB: vector storage and retrival
### code with workflow:

user query (main.py) -> user embeddign(embedding.py) -> search (chroma_store.py) -> retrieve results(advance_rag.py) -> Hybrid search(semention<advance_rag.py>+ keyword_scrore(retriver.py))-> Reranking -> Top context results (reranked.py) -> return to main (main.py) -> ollama genrate anwser(generator.py) -> answer 

    Till now::
        Day 9: Atonomus agent
        Day 10: Advance pallner
        Day 11: Memory integratio (sqlite)
        Day 12: Advace RAG (Chunking, Vecore DB) etc.









