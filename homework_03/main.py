import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "root"}


@app.get("/ping/")
def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
