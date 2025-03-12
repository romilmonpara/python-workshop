import os
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

import openai

client = openai.OpenAI(api_key=OPENAI_API_KEY)
def get_api_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages={"role":"user", 'content':prompt}
    )
    return response.choices[0].message['content']

print(get_api_response("Hello, How are Uhh?"))

# .env file consists OPENAI_API_KEY variable that has OpenAI API Key
# OPENAI_API_KEY = "-----API KEY-----"