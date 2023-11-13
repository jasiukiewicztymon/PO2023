from openai import OpenAI


class Chat:
    MODEL = {
        "GPT_3.5": "gpt-3.5-turbo",
        "GPT_4": "gpt-4"
    }

    def __init__(self, context, api_key, model):
        if (model in list(self.MODEL.keys())):
            self.model = self.MODEL[model]
        else:
            self.model = "gpt-3.5-turbo"

        self.client = OpenAI()
        try:
            self.client.api_key = api_key
            self.valid_key = True
        except:
            self.valid_key = False

        if (context != "" and type(context) == str):
            self.history = [
                {"role": "system", "content": context}
            ]
        else:
            self.history = []

    def set_api_key(self, api_key):
        try:
            self.client.api_key = api_key
            self.valid_key = True
        except:
            self.valid_key = False

    def chat(self, message):
        if (not self.valid_key):
            return {"code": "error", "message": "Invalid API key", "code": 401}

        if (type(message) != str or message == ""):
            return {"code": "error", "message": "Invalid message", "code": 402}
        else:
            self.history.append({"role": "user", "content": message})
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history)

            # print(response.choices[0].message)
            self.history.append(
                {"role": "assistant", "content": response.choices[0].message.content})

            return response.choices[0].message.content
