from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return "version 2 SSH key 삭제해서 CICD 안됨"