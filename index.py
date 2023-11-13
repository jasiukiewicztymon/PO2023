import os
from dotenv import load_dotenv
from ChatOpenAI import Chat

load_dotenv()

c = Chat(None, os.getenv("OPENAI_API_KEY"), Chat.MODEL["GPT_3.5"])

print(c.chat("Quel jour sommes-nous? Donne moi le jour en anglais."))

print(c.history)