import openai
from openai import OpenAI
from source.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
client = OpenAI()


def get_chat_response(message, history):
    history = history or [{'role': 'system', 'content': 'You are a helpful assistant.'}]

    history += [{'role': 'user', 'content': message}]

    completion = client.chat.completions.create(
        model = 'gpt-4.1',
        messages = history,
        temperature = 0.7
    )

    response = completion.choices[0].message

    history += [{'role': response.role, 'content': response.content}]
    return response.content, history
