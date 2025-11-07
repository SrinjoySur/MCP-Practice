from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("Greeting Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()