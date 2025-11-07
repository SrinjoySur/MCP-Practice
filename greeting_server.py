from fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP(
    name="Greeting Server",
    instructions="""
        Greets Any User Who Comes To The Server.
""")

@mcp.tool(name="Greet",description="Greets the user")
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()