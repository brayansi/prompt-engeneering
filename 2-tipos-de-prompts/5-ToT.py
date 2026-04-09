from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from utils import print_llm_result

load_dotenv()
msg1 = """
Você é um engenheiro de software sênior.
Um usuário relata que uma requisição à API no endpoint `/users` está demorando 5 segundos para responder, o que é muito lento.
Pense de forma Tree of Thought:
- Gere pelo menos 3 possíveis causas para essa latência.
- Para cada causa, raciocine passo a passo sobre a probabilidade e como você verificaria.
- Compare os ramos e escolha o mais plausível como hipótese principal.
- Finalize com a próxima ação recomendada para depurar ou corrigir o problema.
"""

msg2 = f"""
Você está projetando um serviço que processa milhões de imagens por dia.
Pense de forma Tree of Thought:
- Gere pelo menos 3 opções diferentes de arquitetura.
- Para cada opção, raciocine passo a passo sobre escalabilidade, custo e complexidade.
- Compare as opções.
- Escolha o melhor custo-benefício e explique por que é superior às demais.
- Finalize com "Resposta Final: " + a opção escolhida.
"""

msg3 = f"""
Você está projetando um serviço que processa milhões de imagens por dia.
Pense de forma Tree of Thought:
- Pense em pelo menos 3 opções diferentes de arquitetura.
- Para cada opção, raciocine passo a passo sobre escalabilidade, custo e complexidade.
- Compare as opções.
- Escolha o melhor custo-benefício e explique por que é superior às demais.
- Finalize com "Resposta Final: " + a opção escolhida em no máximo 6 palavras.

- RETORNE APENAS A RESPOSTA FINAL, SEM NENHUM OUTRO TEXTO.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model


# response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
# response3 = llm.invoke(msg3)

# print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
# print_llm_result(msg3, response3)