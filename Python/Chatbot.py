from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()