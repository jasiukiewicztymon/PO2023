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

# Setting up FastAPI middleware to avoid the 
# cors and no-cors api problem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chats = {}

# Create a new chat with isolated memory
@app.post("/chat/")
async def create_chat(body: str = Body()):
    data = json.loads(body)

    suuid = str(uuid.uuid4())
    chats[suuid] = Chat(str(data['context']) if 'context' in data else None, data['model'] if 'model' in data else '')
    return {"chatid": suuid}

# Send a message to a given chat
@app.post("/chat/{chatid}/")
async def ask_chat(chatid, body: str = Body()):
    data = json.loads(body)

    print(chats[chatid].history)

    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unknown chat ID"}
    else:
        r = chats[chatid].chat(str(data['question']))
        return {"status": "success", "content": r}

# Return the hole chat history
@app.get("/chat/{chatid}/")
async def get_chat(chatid):
    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unfound chat"}
    else:
        return { "status": "success", "content": chats[chatid].history, "model": chats[chatid].model,  }

# App serving staticly the index.html
app.mount("/", StaticFiles(directory="c"), name="static")