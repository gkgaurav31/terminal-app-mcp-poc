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
