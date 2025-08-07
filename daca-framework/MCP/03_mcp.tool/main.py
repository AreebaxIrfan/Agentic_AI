from mcp.server import FastMCP

mcp = FastMCP(name="hello-mcp" , stateless_http=True)

@mcp.tool()
def search_online(query:str)->str:
    return f"Result for {query}.."

@mcp.tool()
async def get_weather(city:str)->str:
    return f"Weather in {city} is sunny"


mcp_app =mcp.streamable_http_app()