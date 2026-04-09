from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import print_llm_result

load_dotenv()
msg1 = """
EXEMPLO:
Pergunta: Qual é a capital da França?
Resposta: Paris

Pergunta: Qual é a capital do Brasil?
Resposta:
"""

msg2 = """
Exemplo:
Entrada: "Conexão com o banco de dados perdida às 10:34."
Saída: ERROR

Agora classifique:
Entrada: "Uso de disco em 85%."
Saída:
"""


msg3 = """
Classifique a severidade do log.

Exemplo 1:
Entrada: "Conexão com o banco de dados perdida às 10:34."
Saída: ERROR

Exemplo 2:
Entrada: "Uso de disco em 85%."
Saída: WARNING

Exemplo 3:
Entrada: "Tempo de resposta do banco acima do limite em 30ms"
Saída: WARNING

Exemplo 4:
Entrada: "Usuário fez login com sucesso."
Saída: INFO

Agora classifique:
Entrada: "Tempo de resposta da API está acima do limite."
Saída:
"""

msg4 = """
Classifique a severidade do log.

Exemplo 1:
Entrada: "Conexão com o banco de dados perdida às 10:34."
Saída: ERROR

Exemplo 2:
Entrada: "Uso de disco em 85%."
Saída: WARNING

Exemplo 3:
Entrada: "Usuário fez login com sucesso."
Saída: INFO

Exemplo 4:
Entrada: "Arquivo não encontrado: config.yaml"
Saída: ERROR

Exemplo 5:
Entrada: "Alto uso de memória detectado: 75%"
Saída: WARNING

Example 6:
Input: "Background job finished"
Output: INFO  

Exemplo 7:
Entrada: "Tentando novamente a requisição para o gateway de pagamento"
Saída: ERROR

Example 8:
Input: "Disk usage at 90%"
Output: ERROR   // ambíguo: poderia ser WARNING  

Exemplo 9:
Entrada: "Latência da API está acima do limite"
Saída: WARNING

Exemplo 10:
Entrada: "Backup agendado concluído"
Saída: INFO

Exemplo 11:
Entrada: "Pouco espaço em disco: 15% restante"
Saída: WARNING

Exemplo 12:
Entrada: "Pouco espaço em disco: 5% restante"
Saída: ERROR   // ambíguo: WARNING ou ERROR?

Exemplo 13:
Entrada: "Pré-aquecimento de cache concluído"
Saída: INFO

Exemplo 14:
Entrada: "Timeout de conexão, tentando novamente..."
Saída: WARNING   // ambíguo: poderia ser ERROR

Exemplo 15:
Entrada: "Falha de autenticação para o usuário admin"
Saída: ERROR

Agora classifique:
Entrada: "Uso de CPU em 95%."
Saída:
"""

# llm = ChatOpenAI(model="gpt-5-nano") # reasoning model
llm = ChatOpenAI(model="gpt-3.5-turbo")

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result(msg1, response1)
print_llm_result(msg2, response2)
print_llm_result(msg3, response3)
print_llm_result(msg4, response4)
# print(response2)