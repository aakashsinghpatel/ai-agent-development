
from pathlib import Path
""" 
    Part of security: Permission chck for tool acces
    This file will be there to handle permission access to each AI agent 
    with respec to access for available tool
    So before executing tool asked by agent check permission are those 
    agent have access to use the tool
    agenname:set of tool name which allow to access by it
"""
TOOL_PERMISSIONS = {
    "research": {"get_weather","read_file"},
    "coding": {"read_file"},
    "review": {"read_file"},
    "manager": {"get_weather","read_file"}
}

""" Prompt Injection: protection technique """ 
# This can be use against prompt injection, where it been asked by agent to delet file
#  so from her can check whether dele file allowed by agent of not
def is_tool_allowed(agent_name,tool_name):
    allowed_tools = (TOOL_PERMISSIONS.get(agent_name,set()))

    return ( tool_name in allowed_tools)

def demonstrate_permissions():
    examples = [("research", "read_file"), ("coding", "get_weather"), ("review", "read_file"),
                ("manager", "get_weather")]

    print("\nPermission Demonstration")
    print("-" * 30)
    for agent_name, tool_name in examples:
        allowed = is_tool_allowed(agent_name,tool_name)
        print(f"{agent_name:10} -> "f"{tool_name:12} : "
            f"{'ALLOWED' if allowed else 'DENIED'}"
        )


""" This below code is relative to worker which have access to specifi folder """
# .resolve() provide absolute path of folder
DOCUMENT_FOLDER = Path("document").resolve()

def safe_file_acess(filename):
    # This code give absolute path to whole file
    path = Path(DOCUMENT_FOLDER/filename).resolve()
    # Below code will check that the resolved file path is relative to folder or not
    # For exaple if someone given filename as ../secure as this will go one folder back:
    # so rather giving direct file path we check if resolved file path realtive to 
    # folder path or not
    if not path.is_relative_to(DOCUMENT_FOLDER):
        raise PermissionError(" Access denied")
    return path

# Before accessing file check if this file secure or not
safe_file_acess("demo.txt")



