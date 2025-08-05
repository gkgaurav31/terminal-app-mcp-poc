from mcp.server.fastmcp import FastMCP
import subprocess

# Create an MCP server
mcp = FastMCP("terminal_tool")

@mcp.tool()
def terminal_tool(command: str) -> str:
    """Run a terminal command and return its output as a string."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        return output.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
