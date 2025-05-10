from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import *
from langchain_core.output_parsers import *
from langchain.chat_models import init_chat_model
from langchain_core.runnables import *
from langchain_core.messages import SystemMessage,HumanMessage
import os
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# # Set your MistralAI API key
os.environ["MISTRAL_API_KEY"] = "OxMn5wJ7YkowO5ly93DvO6HFii0rqezf"

model = ChatMistralAI(
    model="open-mistral-nemo",
    temperature=0,
    max_retries=2,
)

# Memory to keep conversation history
memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=model,
    # memory=memory,
    verbose=True
)


