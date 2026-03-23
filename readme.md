# Prompt Engineering

Repositório de estudo e referência sobre Prompt Engineering, com documentação e exemplos práticos.

## Conteúdo

- **`1-introducao/`** — Documentação:
  - [Introdução ao Prompt Engineering](1-introducao/prompt-engeneering.md) — visão geral, cenários de aplicação, conceitos técnicos e fluxo de estudo recomendado.
- **`2-role-prompts/`** — Exemplos e documentação:
  - [Role Prompts](2-role-prompts/role-prompts.md) — definição explícita do papel do modelo, quando usar, limitações e exemplos práticos.
  - Exemplos `.py` da seção:
    - [`role-prompts.py`](2-role-prompts/role-prompts.py)

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

## Exemplo rápido

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate

# Instalar pacotes principais para estudos com LLMs
pip install -r requirements.txt
```

Ou, para instalação manual dos principais pacotes:

```bash
pip install python-dotenv openai
```

### Principais pacotes utilizados

| Pacote | Descrição |
|--------|-----------|
| **`python-dotenv`** | Carrega variáveis de ambiente de um arquivo `.env` (chaves de API). |
| **`openai`** | Cliente oficial da API OpenAI para interação com modelos GPT. |

### Salvar dependências do ambiente

Depois de instalar os pacotes, gere o arquivo de dependências do projeto:

```bash
pip freeze > requirements.txt
```

Esse comando lista os pacotes instalados no ambiente virtual atual e salva no arquivo `requirements.txt`. Isso facilita reproduzir o mesmo ambiente em outra máquina com:

```bash
pip install -r requirements.txt
```

Use a seção `1-introducao/` como ponto de partida conceitual e `2-role-prompts/` para praticar o primeiro tipo de prompt com exemplos de código.
