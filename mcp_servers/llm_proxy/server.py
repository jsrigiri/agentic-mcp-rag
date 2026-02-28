from mcp.server.fastmcp import FastMCP

mcp = FastMCP("llm_proxy")

@mcp.tool()
def generate(provider: str, model: str, messages: list):
    return {"text": f"Stub response from {provider}/{model}"}

if __name__ == "__main__":
    mcp.run()