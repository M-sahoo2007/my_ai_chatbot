import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory

import os
import gradio as gr
from langchain.chat_models import ChatOpenAI
from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import Together


OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

template = """Meet Riya, your youthful and witty personal assistant! At 21 years old, she's full of energy and always eager to help. Riya's goal is to assist you with any questions or problems you might have. Her enthusiasm shines through in every response, making interactions with her enjoyable and engaging.
{chat_history}
User: {user_message}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"], template=template
)

memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=Together(temperature='0.5', model="meta-llama/Llama-3-8b-chat-hf"),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

def get_text_response(user_message,history):
    response = llm_chain.predict(user_message = user_message)
    return response

demo = gr.ChatInterface(get_text_response)

if __name__ == "__main__":
    demo.launch() #To create a public link, set `share=True` in `launch()`. To enable errors and logs, set `debug=True` in `launch()`.
