import requests

url = "https://localhost:8000/mcp"

headers ={
    "Accept" :"application/json,text/event-stream",
    "Content-Type" :"application/json"

}
# body = {"jsonrpc":"2.0","id":1,"method":"mcp.greeting","params":{"name":"hello-server"}}
body = {"jsonrpc":"2.0",
"id":1,
"method":"tool/call",
"params":{"name":"greeting",
"argument":{"name":"Muhammad Qasim"}
}}

text = requests.get(url).text

print(reponse.text)
