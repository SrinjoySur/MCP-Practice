from fastmcp import FastMCP

mcp = FastMCP(
    name="Simple Calculator",
    instructions="""
        This server provides simple calculation tools.
        Call add() for addition.
        Call substract() for substraction.
        Call divide() for division.
        Call multiply() for multiplication.
""")
@mcp.tool(name="Add",description="Adds 2 numbers")
def add(a:float,b:float)->float:
    return a+b
@mcp.tool(name="Multiply",description="Multiplies 2 number")
def multiply(a:float,b:float)->float:
    return b*a
@mcp.tool(name="Substact",description="Substracts 2 numbers")
def substarct(a:float,b:float)->float:
    return a-b
@mcp.tool(name="Divide",description="Divides 2 numbers")
def divide(a:float,b:float)->float:
    if(a==0 or b==0):
        return 0
    elif(a>b):
        return a/b
    else:
        return b/a
if __name__=="__main__":
    mcp.run()

    