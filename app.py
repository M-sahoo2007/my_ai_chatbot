import os
import gradio as gr
from dotenv import load_dotenv  # NEW: To load your .env file

# Load environment variables
load_dotenv()

# Import updated LangChain modules
from langchain_community.llms import Together
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# Get your API key securely from environment
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Template for chatbot responses
template = """Meet Riya, your youthful and witty personal assistant! At 21 years old, she's full of energy and always eager to help. Riya's goal is to assist you with any questions or problems you might have. Her enthusiasm shines through in every response, making interactions with her enjoyable and engaging.
{chat_history}
User: {user_message}
Chatbot:"""

# Prompt setup
prompt = PromptTemplate(
    input_variables=["chat_history", "user_message"],
    template=template
)

# Memory for conversation
memory = ConversationBufferMemory(memory_key="chat_history")

# LLM setup using Together API key
llm_chain = LLMChain(
    llm=Together(
        model="meta-llama/Llama-3-8b-chat-hf",
        temperature=0.5,
        together_api_key=TOGETHER_API_KEY  # ✅ Secure key loading
    ),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

# Gradio Chat Interface
def get_text_response(user_message, history):
    response = llm_chain.predict(user_message=user_message)
    return response

demo = gr.ChatInterface(get_text_response)

if __name__ == "__main__":
    demo.launch()  # Optional: make it public if needed
