# deployment.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integer numbers
    Args:
        a (int): The first number.
        b (int): The second number.
    """
    return a + b