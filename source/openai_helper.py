import openai
from openai import OpenAI
from source.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
client = OpenAI()


def get_chat_response(message, history):
    history = history or []  # [{'role': 'developer', 'content': 'You are a helpful assistant.'}]

    system_message = 'You are a helpful assistant'

    messages = history + [{'role': 'user', 'content': message}]

    if messages[0].get('role') != 'developer':
        messages = [{'role': 'developer', 'content': system_message}] + messages

    completion = client.chat.completions.create(
        model = 'gpt-4.1',
        messages = messages,  # history + [{'role': 'user', 'content': message}],
        temperature = 0.7
    )

    response = completion.choices[0].message

    messages += [{'role': response.role, 'content': response.content}]  # [{'role': 'assistant', 'content': response}]

    return response.content, messages  # response.content
