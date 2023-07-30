import openai
from dotenv import load_dotenv
import os

openai.api_key = os.getenv('API')

def gpt_res(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    return response["choices"][0]["text"]