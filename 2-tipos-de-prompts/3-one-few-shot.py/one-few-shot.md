# One-shot / Few-shot — Exemplo

O script `one-few-shot.py` mostra como usar **one-shot** e **few-shot prompting**: você dá 1 ou mais exemplos no próprio prompt para “guiar” o modelo no padrão de resposta esperado.

## O que o script faz

1. Faz um **one-shot** com um exemplo de pergunta/resposta sobre capital de país e pede a capital do Brasil.

2. Faz um **one-shot** de classificação, rotulando um log como `ERROR` e pedindo para classificar um novo log.

3. Faz um **few-shot** de classificação de severidade (`ERROR`, `WARNING`, `INFO`) com alguns exemplos e classifica uma nova entrada.

4. Expande para **more-shot** com vários exemplos, incluindo casos **ambíguos**, e pede para classificar um novo log.

5. Exibe as respostas e o uso de tokens com `print_llm_result()`.

## Como rodar

Na raiz do projeto:

```bash
python 2-tipos-de-prompts/3-one-few-shot.py/one-few-shot.py
```

**Pré-requisitos:** `.env` com `OPENAI_API_KEY`, dependências instaladas (`pip install -r requirements.txt`).

