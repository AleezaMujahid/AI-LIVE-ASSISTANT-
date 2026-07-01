from tools import get_weather , calculate , search_web 


#this tells OPENAI what tools exist and what each pparameter meansx
TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function":{
            "name" : "get_weather",
            "description" : "Get current weather for a city using wttr.in (free, no API key needed)",
            "parameters" : {    
                "type" : "object",
                "properties" : {        
                    "city" : {
                        "type" : "string",
                        "description" : "Name of the city to get weather for"
                    }
                },  
                "required" : ["city"]   
            }

        }
    },

    {
        "type": "function",
        "function":{
            "name" : "calculate",
            "description" : "Safely evaluate a math expression",
            "parameters" : {    
                "type" : "object",
                "properties" : {        
                    "expression" : {
                        "type" : "string",
                        "description" : "Math expression to calculate, e.g. (2+3)*4"
                    }
                },  
                "required" : ["expression"]   
            }

        }
    },

    {
        "type": "function",
        "function":{
            "name" : "search_web",
            "description" : "Search using DuckDuckGo instant answers (free, no API key)",
            "parameters" : {    
                "type" : "object",
                "properties" : {        
                    "query" : {
                        "type" : "string",
                        "description" : "Search query to look up on the web"
                    }
                },  
                "required" : ["query"]   
            }

        }
    }

]


#MAP TOOL NAMES TO ACUTAL PYTHON FUNCTIONS

TOOL_FUNCTIONS = {
    "get_weather" : get_weather,
    "calculate" : calculate,
    "search_web" : search_web
}


def run_tool (tool_name: str , tool_args : dict) ->str :
    """Execute the tool the LLM chose and return the result aas a string"""
    if tool_name not in TOOL_FUNCTIONS:
        return f"unknow tool: {tool_name}"
    fn = TOOL_FUNCTIONS[tool_name] 
    return fn(**tool_args)

