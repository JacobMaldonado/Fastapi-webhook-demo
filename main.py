from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.post("/webhook")
def read_item(data: dict):
    print(data)

    return "ok"
