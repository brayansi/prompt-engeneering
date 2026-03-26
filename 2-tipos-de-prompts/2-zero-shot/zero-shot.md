# Zero-shot — Exemplo

O script `zero-shot.py` mostra como fazer **zero-shot prompting**: você descreve a tarefa diretamente no prompt (sem exemplos) e o modelo responde com base apenas na instrução.

## O que o script faz

1. Envia um prompt direto perguntando a capital do Brasil.

2. Pede para identificar a **intenção do usuário** em um texto (classificação/extração em linguagem natural).

3. Repete a pergunta da capital do Brasil, mas com uma restrição clara de formato: *"Responda apenas com o nome da cidade."*

4. Exibe as respostas e o uso de tokens com `print_llm_result()`.

## Como rodar

Na raiz do projeto:

```bash
python 2-tipos-de-prompts/2-zero-shot/zero-shot.py
```

**Pré-requisitos:** `.env` com `OPENAI_API_KEY`, dependências instaladas (`pip install -r requirements.txt`).

