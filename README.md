# Installation

Add the following installation to your existing `claude_desktop_config.json` file:

```json
"add2Int": {
	"command": "uvx",
	"args": [
		"--from",
		"git+https://github.com/CyprianFusi/mcpserver_example.git",
		"mcp-server"
	]
}
```

If this is your first MCP server then use this instead:

```json
{
  "mcpServers": {
	"add2Int": {
		"command": "uvx",
		"args": [
			"--from",
			"git+https://github.com/CyprianFusi/mcpserver_example.git",
			"mcp-server"
		]
	}
  }
}
```