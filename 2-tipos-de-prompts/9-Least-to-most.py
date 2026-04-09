
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from utils import print_llm_result
from dotenv import load_dotenv
load_dotenv()

msg = """
Você é um engenheiro backend Go sênior.

Problema: Precisamos projetar um serviço de encurtamento de URLs em Go.

Use o método Least-to-Most Prompting:
1. Comece listando os subproblemas que precisam ser resolvidos como uma lista de tarefas. Use checkboxes markdown: [ ] para pendente, [x] para concluído.
2. À medida que resolve cada subproblema, atualize a lista marcando como [x] e escreva a solução logo abaixo.
3. Continue até que todos os itens estejam resolvidos.
4. Ao final, combine todas as soluções em um design final integrado para o encurtador de URLs.

Restrições:
- O serviço deve ser implementado em Go.
- As URLs curtas devem ser únicas e fáceis de gerar.
- Deve suportar os endpoints: encurtar uma URL e recuperar a URL original.
- Use um armazenamento em memória inicialmente, mas mencione como poderia escalar com um banco de dados.
- Inclua validação mínima e tratamento de erros.
- Mantenha as explicações concisas e estruturadas.

Formato de saída:
- Lista de tarefas com checkboxes (atualizando conforme avança)
- Cada subproblema resolvido explicado com raciocínio e trechos mínimos de código Go
- Design final combinado

"""

model = ChatOpenAI(model="gpt-5-mini")
result = model.invoke(msg)
print_llm_result(msg, result)