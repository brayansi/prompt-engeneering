# Prompt Engineering

Repositório de estudo e referência sobre Prompt Engineering, com documentação e exemplos práticos.

## Conteúdo

- **`1-introducao/`** — Documentação:
  - [Introdução ao Prompt Engineering](1-introducao/prompt-engeneering.md) — o que é Prompt Engineering e por que importa.
- **`2-tipos-de-prompts/`** — Exemplos práticos de 10 técnicas de prompting:
  - [Referência das técnicas](2-tipos-de-prompts/AGENTS.md) — explicação de cada tipo de prompt com exemplos e quando usar.
  - Scripts: `1-Role-prompts.py`, `2-Zero-shot.py`, `3-One-few-shot.py`, `4-CoT.py`, `4.1-CoT-Self-consistency.py`, `5-ToT.py`, `6-SoT.py`, `7-ReAct.py`, `8-Prompt-channing.py`, `9-Least-to-most.py`

## Pré-requisitos

- [Python 3.10+](https://www.python.org/downloads/) instalado.
- [pip](https://pip.pypa.io/en/stable/installation/) disponível no ambiente.

## Configuração de ambiente

Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Depois, preencha as chaves no `.env`:

- `OPENAI_API_KEY` ou `GOOGLE_API_KEY` (para exemplos com APIs de LLMs, conforme a seção)

## Executando os exemplos

```bash
# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Entrar na pasta de exemplos
cd 2-tipos-de-prompts

# Executar qualquer script
python 1-Role-prompts.py
python 2-Zero-shot.py
python 3-One-few-shot.py
python 4-CoT.py
python 4.1-CoT-Self-consistency.py
python 5-ToT.py
python 6-SoT.py
python 7-ReAct.py
python 8-Prompt-channing.py
python 9-Least-to-most.py

# Desativar quando terminar
deactivate
```

> O script `8-Prompt-channing.py` gera o arquivo `prompt_chaining_result.md` com os resultados encadeados.

### Principais pacotes utilizados

| Pacote | Descrição |
|--------|-----------|
| **`python-dotenv`** | Carrega variáveis de ambiente do arquivo `.env`. |
| **`langchain`** | Framework para interações com LLMs. |
| **`langchain-openai`** | Integração LangChain com a API OpenAI. |
| **`openai`** | Cliente oficial da API OpenAI. |
| **`rich`** | Formatação de saída no terminal. |

### Salvar dependências do ambiente

```bash
pip freeze > requirements.txt
```

Use `1-introducao/` como ponto de partida conceitual e `2-tipos-de-prompts/` para praticar com os exemplos.
