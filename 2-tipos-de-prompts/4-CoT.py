from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Classifique a severidade do log.

Entrada: "Uso de disco em 85%."
Responda apenas com INFO, WARNING ou ERROR.
"""

msg2 = """
Classifique a severidade do log.

Entrada: "Uso de disco em 85%."
Pense passo a passo sobre por que isso é INFO, WARNING ou ERROR.
Ao final, dê apenas a resposta final após "Resposta:".
"""


msg3 = """
Pergunta: Quantas letras "r" existem na palavra "strawberry"?
Responda apenas com o número de "r".
"""

msg4 = """
Pergunta: Quantas letras "r" existem na palavra "strawberry"?
Explique passo a passo separando cada letra em tópicos, destacando os "r" antes de dar a resposta final.
Dê o resultado final após "Resposta:".
"""

llm = ChatOpenAI(model="gpt-3.5-turbo")
# llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)