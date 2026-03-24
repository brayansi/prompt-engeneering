# Role Prompts — Exemplo

O script `role-prompts.py` mostra como o mesmo prompt de usuário gera respostas diferentes conforme o **papel** (role) definido na mensagem de sistema.

## O que o script faz

1. Define dois roles em `system`:
   - **Professor universitário** — explica com definições formais e pseudocódigo
   - **Aluno do ensino médio** — prefere palavras simples e exemplos

2. Faz a mesma pergunta para ambos: *"O que é recursividade em 50 palavras?"*

3. Usa `ChatPromptTemplate` para montar `[system, user]` e invoca o modelo (GPT-4o) duas vezes.

4. Exibe as respostas e o uso de tokens com `print_llm_result()`.

## Como rodar

Na raiz do projeto:

```bash
python 2-tipos-de-prompts/1-role-prompts/role-prompts.py
```

**Pré-requisitos:** `.env` com `OPENAI_API_KEY`, dependências instaladas (`pip install -r requirements.txt`).
