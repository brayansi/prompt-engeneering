from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Você é um engenheiro backend sênior. Um desenvolvedor júnior perguntou como otimizar queries SQL para melhor desempenho.
Siga a abordagem Skeleton of Thought:

Passo 1: Gere apenas o esqueleto da sua resposta em 3–5 tópicos concisos.
Passo 2: Expanda cada tópico com uma explicação clara e detalhada com exemplos.
Certifique-se de que a resposta final seja estruturada e fácil de seguir.
"""

msg2 = f"""
Você é um arquiteto de software. Quero que produza um Architecture Decision Record (ADR) sobre a escolha do PostgreSQL em vez do MongoDB.

Siga a abordagem Skeleton of Thought:
Passo 1: Primeiro, mostre apenas o esqueleto do ADR como cabeçalhos de seção (sem explicações ainda).
Use a estrutura padrão de ADR com 5 seções: Contexto, Decisão, Alternativas Consideradas, Consequências, Referências.
Passo 2: Após mostrar o esqueleto, expanda cada seção com conteúdo claro e detalhado.
Mantenha o ADR final profissional, estruturado e fácil de ler.
"""

msg3 = f"""
Você é um desenvolvedor Go sênior. Quero que me ajude a planejar uma REST API para gerenciamento de produtos em Go.

Siga a abordagem Skeleton of Thought:

Passo 1: Mostre apenas o esqueleto da solução em 6–8 tópicos concisos.
O esqueleto deve cobrir: definição do modelo de dados em Go (structs), escolha do framework HTTP ou net/http, roteamento, handlers, validações, camada de banco de dados, tratamento de erros e estrutura do projeto. Não expanda ainda.

Passo 2: Expanda cada tópico com detalhes técnicos claros, exemplos e boas práticas em Go.
Inclua trechos de código Go (structs, handlers, rotas) e considerações sobre pacotes (ex: chi ou net/http), tratamento de erros idiomático em Go e como organizar o projeto em pacotes (handlers, models, db).
Use linguagem concisa e profissional.

A API deve implementar operações CRUD para produtos com os campos: id, nome, descrição, preço, estoque.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)