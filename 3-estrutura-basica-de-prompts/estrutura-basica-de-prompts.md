# Estrutura Basica de Prompts

## Visao geral

A estruturacao de prompts nao tem formula unica. Cada contexto pede uma estrategia diferente: desenvolvimento de software, agentes, exploracao de ideias, geracao de documentos e automacoes em geral. O objetivo de uma boa estrutura e reduzir ambiguidade, aumentar previsibilidade e alinhar o comportamento da IA ao resultado esperado.

## Por que prompts incompletos geram problemas

Prompts vagos ou sem limites claros podem fazer a IA ser "proativa demais", indo alem do objetivo inicial. No desenvolvimento, isso costuma causar:

- alteracoes desnecessarias em muitos arquivos;
- pull requests maiores que o necessario;
- code review mais lento e mais arriscado;
- perda de foco no objetivo principal (ex.: corrigir apenas um bug urgente).

Licao central: se o prompt nao define limites e saida esperada, o modelo decide por conta propria.

## IA como "novo colega de equipe"

Quando a resposta da IA vier ruim, o caminho produtivo e revisar o resultado e transformar os erros em diretrizes explicitas para os proximos prompts. Em vez de so reclamar, documente:

- o que nao deve ser usado;
- quais padroes devem ser seguidos;
- quais restricoes de tamanho, formato e escopo devem ser respeitadas;
- como ela deve se comportar em casos de duvida.

Com o tempo, isso vira um ativo do projeto e melhora consistencia entre chats.

## Tokens, custo e escala

### Em tarefas pontuais (nao escaladas)

Em desenvolvimento, exploracao e criacao de materiais, geralmente vale priorizar qualidade e contexto, sem excesso de preocupacao com economia de tokens, desde que nao ultrapasse a janela de contexto.

### Em aplicacoes escaladas

Quando ha alto volume via API, o custo por token e a latencia viram fatores criticos. Nesse caso, simplificar prompts e otimizar tokens passa a ser obrigatorio. O trade-off sempre envolve:

- custo;
- latencia;
- qualidade/assertividade.

## Guideline: quando usar zero-shot e few-shot

### Zero-shot

Use para tarefas simples, comuns e de alto volume, com menor custo e menor latencia.

Exemplos: validar formato, identificar informacao direta, resumir texto curto.

### Few-shot

Use quando o dominio e especifico e o formato de saida precisa ser rigoroso. Entrega mais controle, mas custa mais e tende a ser mais lento.

Regra pratica: medir se o ganho de assertividade compensa o aumento de custo.

## Conceito-chave: System Prompt x User Prompt

- **System Prompt**: define regras globais, comportamento, tom e restricoes da conversa.
- **User Prompt**: pedido especifico de cada interacao, que deve respeitar o System Prompt.

Em teoria, o System Prompt tem prioridade, mas pode sofrer tentativas de quebra (prompt injection/jailbreak). Por isso, ele precisa ser bem definido.

## Estrutura recomendada para prompts elaborados

Uma estrutura base reutilizavel:

1. **Persona e escopo**  
   Defina quem o modelo e e o que ele nao pode fazer.

2. **Objetivo**  
   Descreva a tarefa de forma direta e sem ambiguidades.

3. **Entrada**  
   Forneca apenas o contexto necessario, separado visualmente.

4. **Formato de saida**  
   Especifique formato exato (ex.: JSON com campos definidos).

5. **Criterios de qualidade**  
   Liste o que caracteriza uma resposta aceitavel.

6. **Ambiguidades e pressupostos**  
   Diga o que assumir em caso de falta de informacao e como declarar essas suposicoes.

7. **Instrucoes negativas**  
   Declare explicitamente o que nao deve aparecer na resposta.

8. **Tratamento de erro**  
   Defina como retornar falhas quando a tarefa nao puder ser concluida.

## Conclusao

Prompt engineering nao e apenas "escrever um comando". E desenhar comportamento, limites, formato e qualidade da resposta com intencao. Quanto mais estruturado e reutilizavel for o prompt, maior a chance de resultado consistente e menor a chance de retrabalho no fluxo real de desenvolvimento.
