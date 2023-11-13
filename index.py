import os
from dotenv import load_dotenv
from ChatOpenAI import Chat
from typing import Union, Annotated
from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware
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

chats = {

}


@app.post("/chat/")
async def create_chat():
    suuid = str(uuid.uuid4())
    chats[suuid] = Chat(None, os.getenv(
        "OPENAI_API_KEY"), Chat.MODEL["GPT_3.5"])
    return {"chatid": suuid}


@app.post("/chat/{chatid}/")
async def ask_chat(chatid, question: Annotated[list[str] | None, Header()] = None):
    if (chatid not in list(chats.keys())):
        return {"status": "error", "message": "Unknown chat ID"}
    else:
        r = chats[chatid].chat(str(question))
        return {"status": "success", "content": r}


@app.get("/")
def read_root():
    return {"Hello": "World"}

# c = Chat(None, os.getenv("OPENAI_API_KEY"), Chat.MODEL["GPT_3.5"])
# print(c.chat("Quel jour sommes-nous? Donne moi le jour en anglais."))
# print(c.history)
