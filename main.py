from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def hello():
    return "hello"

@app.get("/html")
def hello():
    return FileResponse("index.html")

@app.get("/data")
def data():
    return {"hello" : "1234"}