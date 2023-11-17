import os
import json
from dotenv import load_dotenv
from ChatOpenAI import Chat

from typing import Union, Annotated, Optional
from fastapi import FastAPI, Header, Body
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
async def create_chat(body: str = Body()):
    data = json.loads(body)

    suuid = str(uuid.uuid4())
    chats[suuid] = Chat(str(data['context']) if data['context'] != None else None, os.getenv(
        "OPENAI_API_KEY"), data['model'])
    return {"chatid": suuid}


@app.post("/chat/{chatid}/")
async def ask_chat(chatid, body: str = Body()):
    data = json.loads(body)

    return { 'question': body}

    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unknown chat ID"}
    else:
        r = chats[chatid].chat(str(data['question']))
        return {"status": "success", "content": r}

@app.get("/chat/{chatid}/")
async def get_chat(chatid):
    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unfound chat"}
    else:
        return { "status": "success", "content": chats[chatid].history, "model": chats[chatid].model,  }

app.mount("/", StaticFiles(directory="c"), name="static")