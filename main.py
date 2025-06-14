import gradio as gr
from source.openai_helper import get_chat_response


def chat(message, history):
    response, history = get_chat_response(message, history)
    return response


if __name__ == "__main__":

    demo = gr.ChatInterface(
        fn = chat,
        title = 'Mini ChatGPT',
        type = 'messages'
    )

    demo.launch()
