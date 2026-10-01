Teach your AI Assitant to Read the file

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