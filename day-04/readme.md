Teach your AI Assitant to Use AI Tool

Toosl: Small piece of s/w or python code that do specific task.
each toll should be tested saperately for good enterpricse app.

AI AGent= Reason (check), plan, automatici tool call and response
AI Assitant: Generate response, 
AI Assitant with tool: Python program which when and which tool to be call and assitant just genrate response.

Tool call recognize on keywork matching ("time" i user_input with if else or swith stament)

Code Refactoring: Make code more structure without affecting what it does.
Create tool manager: to handle tool call based on user input
Single and saperate responsibility principle
Modular Architechture.

Till now, out python code (tool manager) decide when and which tool to call available in the system. In futute the tool be be called formmouter system based on the decisicon done by AI agent via function calling.

In future there will be tool availabe that need to be call from external system vai MCP standard.

Till now AI Agent can->
a. Store conversation: Convresation memory.
b. Adopt different personality : System Prompt
c. can use real s/w tool : tool call
d. easy to extend with new tool and responsibility : Tool manager
e. code is cleaner, moduler and manageble: Single and saperate reponsibility with module architechture.


