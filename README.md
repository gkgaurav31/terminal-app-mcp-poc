# MCP Terminal Tool Server

This is a simple MCP server built with the MCP Python SDK. It exposes a single tool called `terminal_tool` that allows users to run terminal commands and returns their output.

## Requirements
- Python 3.8+
- MCP Python SDK (`pip install mcp-sdk`)

## Running the Server

```bash
python server.py
```

## Exposed Tool

### terminal_tool
- **Description:** Run a terminal command and return its output as a string.
- **Arguments:**
  - `command` (str): The terminal command to execute.
- **Returns:**
  - Output of the command as a string (stdout or stderr).

---

**Note:** Use with caution. This tool executes arbitrary shell commands on the server.

## MCP Inspector & Claude Configuration

To connect this server to the MCP Inspector, Claude (Anthropic), or other MCP-compatible clients, use a configuration like the following:

```json
{
  "mcpServers": {
    "terminal_tool": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/project",
        "run",
        "server.py"
      ]
    }
  }
}
```

- Replace `/path/to/your/project` with the absolute path to your project directory.
- This configuration will launch the server using `uv` and connect via stdio transport (default).
- **Claude (Anthropic) users:** You can add this configuration to your Claude MCP settings to enable tool use with your local server.
- For HTTP transport, start the server manually with `python server.py` (or `uv run server.py`) and connect to the appropriate URL in the Inspector.
