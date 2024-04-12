##integrate code with OpenAI API
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory
import langsmith
from dotenv import load_dotenv
load_dotenv()

import langsmith.wrappers
import streamlit as st
import os 

os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = f"test"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("lang")
#prompt
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are good"),
        ("user","Question:{question}")
    ]
)
#streamlit
st.title("Project Demo")
input_text=st.text_input("search")

#ollama

llm=Ollama(model="llama2-uncensored")
Output_Parser=StrOutputParser()
chain=prompt|llm|Output_Parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

