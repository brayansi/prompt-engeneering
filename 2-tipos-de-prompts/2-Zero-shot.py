from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from utils import print_llm_result
from dotenv import load_dotenv

load_dotenv()

msg1 = "Qual é a capital do Brasil?"

msg2 = """
Encontre a intenção do usuário no texto a seguir:
Estou procurando um restaurante na região de São Paulo que tenha boa avaliação de comida japonesa.
"""

msg3 = "Qual é a capital do Brasil? Responda apenas com o nome da cidade."

llm = ChatOpenAI(model="gpt-4o")

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)