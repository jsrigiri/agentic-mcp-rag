from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sql")

@mcp.tool()
def sql_query(query: str):
    return {"query": query, "rows": []}

if __name__ == "__main__":
    mcp.run()