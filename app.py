import gradio as gr
from source.openai_helper import get_chat_response
from source.chat_storage import save_chat, list_saved_chats, load_chat


def chat(message, history):
    response, updated_history = get_chat_response(message, history)
    return updated_history, updated_history  # response, history


def save_current_chat(history_state):
    filename = save_chat(history_state)
    return f'Saved as {filename}'


def load_selected_chat(filename):
    if filename:
        chat_history = load_chat(filename)
        return chat_history, chat_history
    return [], []


def refresh_dropdown():
    return gr.update(choices = list_saved_chats())


if __name__ == '__main__':
    with gr.Blocks() as demo:
        state = gr.State([])

        with gr.Row():
            # Sidebar
            with gr.Column(scale = 1):
                gr.Markdown('### 📂 Saved Chats')
                chat_selector = gr.Dropdown(label = 'Select a chat', choices = list_saved_chats())
                refresh_button = gr.Button('🔄 Refresh List')
                load_button = gr.Button('▶️ Load Selected Chat')
                save_button = gr.Button('💾 Save Current Chat')
                save_status = gr.Textbox(label = 'Save Status', interactive = False)

            # Main chat area
            with gr.Column(scale = 4):
                gr.Markdown("## 💬 ChatGPT Gradio App")

                chatbot = gr.Chatbot(
                    type = 'messages',
                    height = 300
                )

                txt_input = gr.Textbox(label = 'Enter your message here')
                txt_input.submit(chat, [txt_input, state], [chatbot, state]).then(lambda: "", None, [txt_input])

                # gr.ChatInterface(
                #     fn = chat,
                #     title = '💬 ChatGPT Gradio App',
                #     type = 'messages',
                #     chatbot = chatbot,
                #     textbox = txt_input,
                #     additional_outputs = state
                # )

                send_btn = gr.Button('Send')
                # clear_btn = gr.ClearButton(txt_input, value = 'Clear')
                # clear_btn.click(clear, [], [])

        # Functional bindings
        send_btn.click(chat, [txt_input, state], [chatbot, state]).then(lambda: "", None, [txt_input])
        save_button.click(save_current_chat, [state], [save_status])
        load_button.click(load_selected_chat, [chat_selector], [chatbot, state])
        refresh_button.click(refresh_dropdown, [], [chat_selector])

    demo.launch()
