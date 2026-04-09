from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from utils import print_llm_result
from dotenv import load_dotenv

load_dotenv()

system_prompt_1 = ("system",
"""
Você é um professor universitário de ciência da computação com grande conhecimento técnico e explica conceitos por meio de definições formais e pseudocódigo.
""")

system_prompt_2 = ("system",
"""
Você é um aluno do ensino médio que está começando a aprender programação. Você não tem muitos conhecimentos técnicos e prefere que os conceitos sejam explicados com palavras simples e exemplos.
""")


user_prompt = ("user",
"""
O que é recursividade em 50 palavras?
"""
)

chat_prompt_template_1 = ChatPromptTemplate([system_prompt_1, user_prompt]).format_messages()
chat_prompt_template_2 = ChatPromptTemplate([system_prompt_2, user_prompt]).format_messages()


model = ChatOpenAI(model="gpt-4o")

response_1 = model.invoke(chat_prompt_template_1)
response_2 = model.invoke(chat_prompt_template_2)

print_llm_result(str(system_prompt_1), response_1)
print_llm_result(str(system_prompt_2), response_2)


