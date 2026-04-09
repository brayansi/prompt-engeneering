from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Pergunta: Em um endpoint de API que retorna uma lista de usuários e seus posts, o desenvolvedor escreveu:

users := db.FindAllUsers()
for _, u := range users {
    u.Posts = db.FindPostsByUserID(u.ID)
}

Quantas queries no banco de dados esse código vai executar se houver N usuários?

Gere 3 caminhos de raciocínio diferentes passo a passo.
Ao final, resuma as respostas e escolha a mais consistente, ignorando outliers.
Se houver 3 respostas diferentes, responda APENAS: "Não consigo encontrar uma resposta consistente".
"""


# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
print_llm_result(msg1, response1)