from mcp.server.fastmcp import FastMCP

mcp = FastMCP("rag_vector")

@mcp.tool()
def retrieve(query: str, k: int = 6):
    return {"query": query, "results": []}

if __name__ == "__main__":
    mcp.run()