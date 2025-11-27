from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from fastmcp import FastMCP
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as ec

mcp = FastMCP(name="Healenium MCP Server",
              instructions="MCP server to heal UI test cases using Healenium."
)
current_webdriver:webdriver.Remote
def getLocator(by:str,value:str)->tuple:
    if by==str.lower(By.ID):
        return (By.ID, value)
    elif by==str.lower(By.CLASS_NAME):
        return (By.CLASS_NAME,value)
    elif by==str.lower(By.LINK_TEXT):
        return (By.LINK_TEXT,value)
    elif by==str.lower(By.PARTIAL_LINK_TEXT):
        return (By.PARTIAL_LINK_TEXT,value)
    elif by==str.lower(By.CSS_SELECTOR):
        return (By.CSS_SELECTOR,value)
    elif by==str.lower(By.XPATH):
        return (By.XPATH,value)
    elif by==str.lower(By.TAG_NAME):
        return (By.TAG_NAME,value)
    else:
        return (by, value)
def getWait(driver:webdriver.Remote)->WebDriverWait:
    return WebDriverWait(driver=driver, timeout=360)
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
@mcp.tool(name="Find-Element",description="Tool To Find A Web Element")
def findElement(by:str,value:str)->str:
    try:
        locator=getLocator(by,value)
        getWait(current_webdriver).until(ec.visibility_of_element_located(locator))
        return "Element Found"
    except NoSuchElementException as e:
        return f"Element not found: {e}"
@mcp.tool(name="Click-Element",description="Tool To Click A Web Element")
def clickElement(by:str,value:str)->str:
    try:
        locator=getLocator(by,value)
        element=current_webdriver.find_element(*locator)
        getWait(current_webdriver).until(ec.element_to_be_clickable(element))
        element.click()
        return "Element Clicked"
    except NoSuchElementException as e:
        return f"Element not found: {e}"
@mcp.tool(name="Close-Browser",description="Closes current Browser Session")
def closeBrowser():
    current_webdriver.close()
if __name__=="__main__":
    mcp.run()