import os
from dotenv import load_dotenv
from ChatOpenAI import Chat

from typing import Union, Annotated
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uuid

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chats = {}


@app.post("/chat/")
async def create_chat(context: Annotated[list[str] | None, Header()] = None, model: Annotated[list[str] | None, Header()] = None):
    suuid = str(uuid.uuid4())
    chats[suuid] = Chat(str(context) if context != None else None, os.getenv(
        "OPENAI_API_KEY"), model)
    return {"chatid": suuid}


@app.post("/chat/{chatid}/")
async def ask_chat(chatid, question: Annotated[list[str] | None, Header()] = None):
    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unknown chat ID"}
    else:
        r = chats[chatid].chat(str(question))
        return {"status": "success", "content": r}

@app.get("/chat/{chatid}/")
async def get_chat(chatid):
    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unfound chat"}
    else:
        return { "status": "success", "content": chats[chatid].history, "model": chats[chatid].model,  }


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.mount("/", StaticFiles(directory="c"), name="static")