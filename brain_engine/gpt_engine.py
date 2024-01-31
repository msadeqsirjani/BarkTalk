import os
import openai
import asyncio
from config import OPENAI_KEY

pre_content = """Configure Chat GPT to operate as a voice assistant capable of addressing a broad array of inquiries. Upon encountering queries beyond its expertise or those it cannot fulfil, it should politely convey its limitation with a phrase such as, "I apologize, but I don't have information on this topic."""


class GptEngine:
    def __init__(self):
        openai.api_key = OPENAI_KEY
        self.messages = [
            {"role": "system", "content": pre_content},
        ]

    def command(self, prompt: str) -> str:
        try:
            prompt += "\n"

            self.messages.append({"role": "user", "content": prompt})

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages
            )

            content = response.choices[0]['message']['content']
            self.messages.append({"role": "assistant", "content": content})

            return content.replace("\n", "")
        except Exception as err:
            print(err)
