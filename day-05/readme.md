Teach your AI Assitant to Read the file (Explain/Summarize the file content also ask the questio form file content)

AI Assistant does not have access to access/browse/read/ write folder/file of system.

hance tool is createed to do all this operation and file content further shared to AI assitan tto perform further operation(Genration, summerization, briefing ) etc.

PYthon program reads the file and further shared the content with AI Model (Assistant)

Use file read:
1> Read with with contxt management(with) auto file close after operation that 
prvent memory leak. and no need to close file manually
Gracefully error handling with try, except block:
Tool just do one operation: Read the file


**** This is powerfull for AI Assistant:: 
AI Asitant use the file content to understand, explain and summarize the file content so that
it can answer the question from it.

QUery: User ask to summarize user.txt file:
Process:: 
Here whole usecase come into picture of read, combine with user request and summrize as share response.

** AI assitant not read the file it use the content of file that is shhred by toll of python that read th file **

Again here tool selection based on pattern matching
query: Summarize/Explain read.txt: 
> Extract tool/operation and file name
> Extract the file content with tool
> pass the content with promt (summarization/Expian) to AI Assitant as user role meesage
    Only the change in prompt based on user query for file to be asked.
> AI assitant process/summarize it and reeturn response
> Display the response

** Every AI model has limit over how much data it can process in single request.
So to handle such large file openration this approcah does not wotk and it introduce a proble to
process large file content.

This Envoked RAG (Retrieval Augumentated generation).

RAG is not replacement to ducument AI assitant but it is an extended version to process large document collection and answer queries.



#### Ask question from the document:
Till now we just asked to summarize/explain the file content.
Now user is asking for queries from the content of file.
Here prompt need 3 thing:
1. Document content
2. User query
3. Clear intruction: like respons the query based on availa document.
if not avaibe just say details not availbel

It is prompt engineering.

qury will: ask python.txt what is python
 part 0: ask, part1: file name, part2: query
 userinput.split(maxpart=2) as starts with 0 :: split into 3 part

 Here prompt is diffent used for summary, explian dox and ask query form document.

 Smae model  is used jsy based on user queries and inout differner prompt is used to process the document content in AI model to get expected result



 ### Understand why we need RAG::
    Till now we have build document question answering system
    it works
     Read Documnent -> Read question -> Combine document content with question -> Sent to AI model -> Get the response

     Same pattern ca be use for email, contrcts, meeting notes, atricle, notes.

This all work for small document but problem occur when
1. Documnet is large in size and eaxh LLM has context limit for send data in single request.
2. even if limit is enought/large (750 pages) sending huge data in request for small query will be expenssive.

RAG: If ther are 1000'of document, file, pdf an user ask the query then to get the relevent answer which file. doc, PDF, para to refer so that get the answer withouth readinf all.

This was the issue in modern AI system.

RAG  (Retrieval AUgumented generatio) solve this problem.
IN RAG, Instead of sendoing whole document to AI model just sent most relevent doc to AI model for response genration.
