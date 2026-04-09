# Tipos de Prompts

Guia de referência sobre as técnicas de prompting demonstradas nos scripts deste diretório.

---

## 1. Role Prompting — `1-Role-prompts.py`

Atribui um papel ou persona ao LLM antes de fazer a pergunta. Influencia o tom, o nível de detalhe e o estilo da resposta.

```
"Você é um engenheiro sênior de backend. Explique o que é um índice de banco de dados."
```

**Quando usar:** sempre que o contexto ou a especialidade do respondente importar para a qualidade da resposta.

---

## 2. Zero-Shot — `2-Zero-shot.py`

Faz uma pergunta direta sem fornecer exemplos. O modelo responde com base apenas no conhecimento pré-treinado.

```
"Classifique o seguinte texto como positivo, negativo ou neutro: 'O produto chegou no prazo.'"
```

**Quando usar:** tarefas simples, bem definidas e que o modelo já conhece bem.

---

## 3. One-Shot / Few-Shot — `3-One-few-shot.py`

Fornece 1 ou mais exemplos de entrada e saída antes da tarefa real. Ensina o modelo o formato ou padrão esperado.

```
Entrada: "O servidor caiu." → Saída: ERROR
Entrada: "Uso de CPU em 60%." → Saída: ?
```

**Quando usar:** quando o formato de saída for específico ou o domínio for especializado.

---

## 4. Chain of Thought (CoT) — `4-CoT.py`

Instrui o modelo a pensar passo a passo antes de dar a resposta final. Melhora muito o desempenho em tarefas de raciocínio.

```
"Pense passo a passo antes de responder."
```

**Quando usar:** matemática, lógica, diagnósticos, análise de código — qualquer tarefa que exija raciocínio encadeado.

---

## 5. CoT com Auto-Consistência — `4.1-CoT-Self-consistency.py`

Extensão do CoT: gera múltiplos caminhos de raciocínio independentes e escolhe a resposta mais consistente entre eles.

```
"Gere 3 caminhos de raciocínio diferentes. Ao final, escolha a resposta mais consistente."
```

**Quando usar:** decisões críticas onde erros têm alto custo e a confiabilidade importa mais que a velocidade.

---

## 6. Tree of Thoughts (ToT) — `5-ToT.py`

O modelo explora múltiplos ramos de raciocínio simultaneamente, avalia cada um e escolhe o mais promissor — como uma árvore de decisão.

```
"Gere pelo menos 3 hipóteses. Para cada uma, avalie viabilidade e custo. Escolha a melhor."
```

**Quando usar:** problemas de planejamento, arquitetura ou estratégia onde há múltiplas soluções possíveis.

---

## 7. Skeleton of Thought (SoT) — `6-SoT.py`

O modelo primeiro gera o esqueleto (estrutura/tópicos) da resposta, e só depois expande cada parte com detalhes.

```
"Passo 1: liste apenas os tópicos principais.
 Passo 2: expanda cada tópico com explicações e exemplos."
```

**Quando usar:** geração de documentos longos, ADRs, relatórios técnicos — qualquer conteúdo que precise de estrutura clara.

---

## 8. ReAct — `7-ReAct.py`

Alterna entre **raciocínio** (`Pensamento:`) e **ação** (`Ação:`), seguido de uma **observação** (`Observação:`). Simula o comportamento de um agente que age e reflete sobre os resultados.

```
Pensamento: o endpoint retorna 500, pode ser problema de query.
Ação: verificar o handler e a query SQL.
Observação: a query usa placeholder incorreto.
Resposta Final: corrigir o placeholder na query.
```

**Quando usar:** debugging, diagnósticos, simulação de agentes que interagem com ferramentas ou sistemas externos.

---

## 9. Prompt Chaining — `8-Prompt-channing.py`

Divide uma tarefa complexa em prompts menores encadeados: a saída de um prompt vira a entrada do próximo. Cada etapa pode usar um modelo diferente.

```
Spec do produto → [LLM 1] → JSON Schema → [LLM 2] → Rotas Go → [LLM 3] → Commit message
```

**Quando usar:** pipelines de geração de código, transformação de dados em múltiplos estágios, fluxos onde cada etapa exige foco distinto.

---

## 10. Least-to-Most — `9-Least-to-most.py`

Decompõe o problema em subproblemas do mais simples ao mais complexo. Resolve cada um na ordem e usa as soluções anteriores para construir a resposta final.

```
"Liste os subproblemas como checkboxes. Resolva cada um em ordem e combine tudo no final."
```

**Quando usar:** problemas algorítmicos, design de sistemas, qualquer tarefa que possa ser resolvida de forma incremental.

---

## Guia Rápido de Escolha

| Técnica | Melhor Para |
|---------|-------------|
| Role Prompting | Ajustar tom e especialidade |
| Zero-Shot | Tarefas simples e diretas |
| Few-Shot | Formato de saída específico |
| CoT | Raciocínio lógico e análise |
| CoT Auto-Consistência | Alta confiabilidade em decisões críticas |
| Tree of Thoughts | Exploração de múltiplas alternativas |
| Skeleton of Thought | Documentos estruturados e longos |
| ReAct | Simulação de agentes e debugging |
| Prompt Chaining | Pipelines com múltiplos estágios |
| Least-to-Most | Decomposição incremental de problemas |
