from mcp.server.fastmcp import FastMCP


# Initialize FastMCP server with enhanced metadata for 2025-06-18 spec
mcp = FastMCP(
    name="hello-server",
    stateless_http=True # When true we don't need handshake or initialize things.
)

@mcp.tool()
def greeting(name:str)->str:
    "greeting user"
    return f"Hello {name}!"

app_mcp = mcp.streamable_http_app()