from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fastmcp import FastMCP


mcp = FastMCP(name="Healenium MCP Server",
              instructions="MCP server to heal UI test cases using Healenium."
)
# nodeURL = "http://localhost:8085"
# options = webdriver.ChromeOptions()
current_webdriver:webdriver.Remote
@mcp.tool(name="Start-Browser",description="Starts Browser")
def startBrowser():
    global current_webdriver
    current_webdriver=webdriver.Remote(
    command_executor="http://localhost:8085",
    options=webdriver.ChromeOptions()
    )
@mcp.tool(name="Navigate-To",description="Navigates to Website")
def navigate(url:str)->None:
    current_webdriver.get(url=url)
@mcp.tool(name="Close-Browser",description="Closes current Browser Session")
def closeBrowser():
    current_webdriver.close()
if __name__=="__main__":
    mcp.run()