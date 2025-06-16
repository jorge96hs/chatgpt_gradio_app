import openai
from openai import OpenAI
from source.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
client = OpenAI()


def get_chat_response(message, history):
    history = history or [{'role': 'developer', 'content': 'You are a helpful assistant.'}]

    system_message = 'You are a helpful assistant'

    # if history:
    #     if history[0].get('role') != 'developer':
    #         history += [{'role': 'developer', 'content': system_message}]

    messages = history + [{'role': 'user', 'content': message}]

    # completion = client.chat.completions.create(
    #     model = 'gpt-4.1',
    #     messages = history + [{'role': 'user', 'content': message}],
    #     temperature = 0.7
    # )

    response = 'No'  # completion.choices[0].message

    messages += [{'role': 'assistant', 'content': response}]  # [{'role': response.role, 'content': response.content}]
    return response, messages  # response.content
