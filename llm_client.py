from langchain_openai import ChatOpenAI
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


class LLMClient:
    def __init__(self, model="llama3-70b-8192", base_url="http://localhost:11434/v1"):
        os.environ["OPENAI_API_KEY"] = "NA"
        #self.llm = ChatOpenAI(model=model, base_url=base_url)
        self.llm = ChatGroq(model_name=model)
    
    def get_llm(self):
        return self.llm


