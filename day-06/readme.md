## Build your first RAG System
### Why do we need RAG?
Till now we are able to explain, summarize and get answer from the document passed.
Read DOc -> QUery + content -> AI model -> Response
But if there is 100 document each having 1000 page then via this approach to get response of small query would be

* Slow, * Expensive * MAny AI model wont support too much conyent in single doc.

Hense smarter sulution is `RAG - Retrieval AUgumentation Genration`.

Retieval: Retrive only relvent document rather reading whole document.
Generation: Generate the response from relevent retrieved data.

Built Simple RAG:

User Query --> Get Relevent Answer -> Sent to AI -> Get Response
Step -1         Step 2                 STep 3       Step 4
ALL things like Embedding, Vector DB are part of step 2.

We are builing by end:
 Query -> Search into Knowledge base -> Get relevent document -> Sent to AI Model -> Get the response

 Knowledge Base: Set of document from which response of query to be expected.

 Document retriever: Get the documents content from Knowledge base

 ** code **
 > from pathlib import path
 * folder = path('knowledge') : to load the name d folder
 * for file in folder.glob('*.txt'): Get alll text file via glob and loop each file
   ** content = file.read_txt(encoding='utf-8') :: Get the content fof all tetx file (utf-8: text file)


 Step 1 : Create Retriever: That read content from Knowlege base 
  Retriver.py->
    load_document(): Load the document from knowledge and store as dict
    retieve(): retieve the file name name and content based on the keyword matching or simple search word contains
      like: python in python.txt content then return respecive file name and content
    Here the retriever is based on keyword based matching.
    
    #### Limitation:
      Only return the first matched not the best match.
      Here the retrieval is based on keyword matching not meaning like: Prograaming and coding is similar in meaning but return for programming only

### Embedding and semactic search: 
  Embedding : Numerical reprsentation of word/sentance.
      It is list of numbers called vectors.
      Ebbedding allow computer to compare sementic meaning rather exact word match.

      Embedding makes Retriever smarter. as it make sementci search over keyword search.
      Embedding of words/sentance leis near to each other which has similar sementci meaning which diffent lies far away.

      text -> embedingg (List of number) -> Vectors.


    why to convert into numerical/number?
    As computer excellent at number comparision therefor convert to embedding.
    Oce text are number then it is easy to say:
      how similar two sentance?
      which pera are closest?
      which document best matches the search,

    Embedding are created by pre-trained llm model.

    Text -> Embedding model -> Vectors
    Mostly hears, embeding are 384, 768, 1536 diamentional.
    Only good embedding metter diamention not metter for ai engineer.
    Embedding model: nomic-embed-text
      why: free, open source, fast , work locally, no need of cloud service.


  *Note: Just pull the model with ollam and start using with openAI sdk there is not need to run the model in cammnd line as via URL call model get auto load into memory and execute.

  > Ollama pull nomic-embed-text

  > response = client.embeding.create(model, input)

  Different model or version generate differnt embeding.
  Model genrate same length of embedding for all text/pera/document of fixed diamention or length.

### from embedding to sementic search:
 embedding is the fixed length multi dimentail vector representation of text/document.
 each embedding will be fixed length.

 But how to compare which embedding is best match: like which documen tto be use for answer the query.

 Here we use : Cosine similarity: FInding the best match document.
 Cosine simility provide the score between tow vector that how that sematicaly similar.

 score:
  1.00 : Sementically identical  .9:Almost identical
  .7: fairly similar, .30: waely simialr, 0.0: un matched 

  The higher the score the most similar the vector and embedding.
  When the two vector score is high they are that identical and as low the score that are far away with same sementic meaning.

  To calculte cosine similarity::

  Uses: Python numpy library: This lib use in python for varios nummerical computation.

  > pip install numpy  

   similarity.py and test_embedding use to experiment this. 
   Tool for find cosine similarity:: cosine_similarity


Sementic retriever:
  Embedding is useful when compared else no useful.
  higher the similarity score more the relevent information
  Now the comparision is not on matching of keyword but on meaning.

  Build complete RAG:
  1. Load Document
  2. Create embeding of document.
  3. retirve most relevent info
  4. use AI model to answer most relevent answer based on knowledge


  ##### Build full RAG workflow from scratch:
  Step 1: Load documennt : tool: >load_document : Dict {filename: content}
  step2: Generate embediing of documnent: tool: create_embedding
    document_embedding{filename: documenentembedding}

    step 1 and 2 are one time activity as it there 1000's of document the each time generation  is not usefull so it improve for best enterprose app
  step 3: Generate embedding of question
    question embedding: create_embedding
  step 4: compare embedding: tool: compate_embedding
    compare the embedding of question with each document embedding and find the nest match scrore and respective document and file name

    Best score, filename
  step 5: Retieve the content
    get the content for the best file
  step6: Buld the prompt
    combine the prompt with content and question

    we only send the required document which has hifger similarity score not whole knowledge base.

    RAG: Only pass the content/context of document which has higher similarity score rhather whole knowledge base to answer the user query.

  step 7:Ask the AI mode: send the prompt


without RAG AI model response to question based on trained data.
But with RAG AI model response based on the required details /info get from knowledge base.
can be use for real time data acces: product info, policyies etc.
No need to train model again and again.


Limitation:
  1. It embed whole document once: what is document has 200page
  2. every time program start generte document embed again: can 't we cache it 
  3. Only only best metch doc is reteived: what if multi document has info
  4. retrieve whole document: can t only retrie para, page only reured part?

  Can be acheable :: Yes

  The professional RAG system solve this using:
    chunking, persistant Vector store, top-k retreival, re-ranking, metadata filterring and hybrid search.

    This are improvements, not new idea the workflow the same.

    Means retrieve relevent information first and generate the answer from AI Model.


### RAG system :: rag.py
1. Load the document
2. create and store embedding of document
  tool: create_embedding
3. Create embedding of question
 use tool
4. compare the embeding
5. Retrive the best match document
6. create the prompt
6. Generate the response with sending prompt to AI model





  
    


