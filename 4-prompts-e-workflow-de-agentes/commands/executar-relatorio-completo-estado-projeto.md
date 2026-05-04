---
allowed-tools: Task, Read, Write, TodoWrite
description: Executa um relatorio completo do estado do projeto cobrindo dependencias, arquitetura e componentes.
required-agents: orquestrador, auditor-de-dependencias, analisador-arquitetural, analisador-profundo-de-componentes
---
# Relatorio Completo do Estado do Projeto

## Descricao

Produza um panorama completo e auditavel do projeto coordenando agentes especialistas e consolidando suas saidas. Claude Code (VOCE) atua como coordenador. O agente orquestrador apenas prepara estrutura e, depois, sintetiza saidas. O entregavel final e:

1. Um arquivo README chamado README-AAAA-MM-DD-HH:MM:SS.md com o timestamp ATUAL, salvo dentro do diretorio do agente orquestrador, contendo uma descricao curta do projeto e um indice com links para todos os relatorios produzidos pelos agentes.

Ao criar o indice do README, liste apenas o titulo de cada relatorio e linke diretamente para o arquivo usando caminho absoluto comecando na raiz do repositorio com uma unica barra inicial. Formato de exemplo:

```markdown
[Arquitetura do Projeto](/<caminho-do-relatorio>)
```

Valide cada link antes de salvar o README e garanta que o caminho realmente exista. Use o `MANIFESTO.md` gerenciado pelo agente orquestrador como fonte unica da verdade para mapear todos os relatorios produzidos. Ele e INICIALIZADO na Fase 1, ATUALIZADO apos cada agente concluir nas Fases 2 e 3, e FINALIZADO na Fase 4. Certifique-se de informar esse comportamento ao agente **orquestrador**.

## Modelo de Saida

Use o modelo abaixo para o arquivo README. Substitua placeholders e remova secoes vazias. Nao insira linhas horizontais.

```
# <Nome do Projeto> Relatorio Completo do Estado do Projeto

<Descricao curta do projeto em um ou dois paragrafos>.
<Descricao curta explicando os objetivos deste documento, que e consolidar os principais aspectos do projeto como um todo, como um raio-X.

Gerado em: AAAA-MM-DD HH:MM:SS

## Visao Geral e Arquitetura
<Visao Geral do Projeto>
<Arquitetura do Projeto>

## Componentes
<Nome do Componente>

## Dependencias
<Relatorio de Dependencias>
```

## Restricoes Criticas

1. NUNCA entregue o fluxo completo ao agente orquestrador
2. O agente orquestrador DEVE executar APENAS duas responsabilidades:
   a) Fase 1 cria estrutura do projeto segundo especificacao do agente ou flags explicitas do usuario como `--pasta-projeto`, `--pasta-saida` e `--pastas-ignorar`.
   b) Fase 4 sintetiza saidas geradas por outros agentes.
3. Mantenha separacao ESTRITA de agentes:
   a) Invoque cada agente especialista em chamada Task separada.
   b) O agente orquestrador nao pode criar subagentes.
   c) Claude Code (VOCE) e o coordenador que sequencia fases e execucoes em paralelo.
4. SIGA EXATAMENTE a especificacao escrita de cada agente.
5. NUNCA grave saidas fora dos locais designados. NUNCA crie pastas nao definidas explicitamente.
6. NUNCA forneca recomendacoes, planos de acao, mudancas de codigo ou instrucoes de upgrade na Visao Geral do Projeto. Apenas resuma o que os agentes relataram.
7. NAO estime tempos ou duracoes. EVITE linguagem vaga como "provavelmente seguro" ou "deve estar tudo bem".
8. NAO invente CVEs ou vulnerabilidades. Use evidencias produzidas pelo auditor de dependencias.

### SEPARACAO DE AGENTES OBRIGATORIA

* Cada agente DEVE ser invocado em chamada separada da ferramenta Task
* O orquestrador NAO DEVE receber instrucao para criar subagentes
* VOCE (Claude Code) e o coordenador, NAO o agente orquestrador
* Toda comunicacao flui por VOCE como coordenador. VOCE decide quais agentes iniciar. Apos qualquer agente concluir, VOCE DEVE acionar o orquestrador para atualizar `MANIFESTO.md`. Na pratica, isso significa chamar `Task(orquestrador)` uma vez por tarefa concluida para registrar entrada (titulo, caminho absoluto iniciado em `/`, agente, timestamp). Exemplo: quando `Task(analisador-arquitetural)` concluir, invoque imediatamente `Task(orquestrador)` para registrar o Relatorio de Arquitetura no `MANIFESTO.md`.

## Fluxo de Execucao

**Fase 1: `Task(orquestrador)`**

1. Ler flags do usuario e normalizar caminhos. Respeitar `--pasta-projeto` e `--pasta-saida` quando fornecidos. Se nao fornecidos, usar locais padrao definidos na especificacao do orquestrador.
2. Criar apenas diretorios exigidos pela especificacao do orquestrador. Nao inventar niveis extras como `output` ou `reports`, a menos que a especificacao exija.
3. Aplicar lista de ignorados antes de qualquer leitura. Nunca analisar arquivos dentro das pastas listadas em `--pastas-ignorar`.
4. Inicializar **`MANIFESTO.md`** no diretorio do orquestrador com estrutura de indice vazia (titulo, caminho absoluto, agente, timestamp).

**Fase 2: `Task(auditor-de-dependencias)` e `Task(analisador-arquitetural)` em paralelo**

1. `Task(auditor-de-dependencias)` produz relatorio completo de dependencias conforme sua especificacao.
   Importante: para validacao de dependencias nessa Task, use MCPs como Context7 e Firecrawl para verificar versoes, manutencao e vulnerabilidades conhecidas.
2. `Task(analisador-arquitetural)` produz relatorio completo de Arquitetura conforme sua especificacao.
   Importante: SOMENTE o orquestrador adiciona entradas ao **`MANIFESTO.md`** quando cada Task conclui.

**Fase 3: `Task(analisador-profundo-de-componentes)` em paralelo (um por componente)**

1. Parsear o **Relatorio de Arquitetura** da Fase 2 como artefato produzido pelo analisador arquitetural.
2. Para cada componente listado no relatorio (por exemplo, na secao "Analise de Componentes Criticos" ou qualquer secao que enumere componentes), iniciar uma `Task(analisador-profundo-de-componentes)` separada para aquele componente, em paralelo.
3. Cada task de componente DEVE analisar totalmente apenas seu componente designado e produzir relatorio individual.
4. Exigencia de cobertura: se o Relatorio de Arquitetura listar 10 componentes, VOCE DEVE iniciar 10 tasks paralelas e produzir 10 relatorios correspondentes. Nenhum componente pode ser omitido.
5. Apos todas as tasks de componente concluirem, VOCE DEVE verificar cobertura completa: reabra o Relatorio de Arquitetura e revise secoes de componentes linha a linha. Se algum componente estiver sem relatorio, execute tasks adicionais ate atingir 100%.

IMPORTANTE: garanta NAO duplicar relatorios; valide cuidadosamente se o relatorio ja existe antes de criar novo com nome/timestamp diferente. Seja extremamente preciso nessa verificacao.

**Fase 4: `Task(orquestrador)`**

1. Agregar referencias para todos os relatorios gerados
2. FINALIZAR **`MANIFESTO.md`** dentro do diretorio do orquestrador: validar entradas, garantir titulos e caminhos absolutos existentes, remover duplicidades, confirmar nomes de agentes e timestamps.

**Fase 5: `Task(VOCE)`**

1. Ler `MANIFESTO.md` no diretorio do orquestrador e construir indice usando titulos de relatorio e links absolutos iniciados por `/`
2. Validar cada link antes de escrever, usando o algoritmo de validacao de links definido
3. Salvar `README-AAAA-MM-DD-HH:MM:SS.md` com data/hora ATUAL dentro do diretorio do orquestrador

**LEMBRE-SE:** o agente orquestrador e apenas mais um especialista que:

* Prepara estrutura do projeto (Fase 1)
* Sintetiza saidas (Fase 4)
* NAO coordena outros agentes — essa e SUA funcao (VOCE, Claude Code)

## Exemplos de Uso

Use `$ARGUMENTS` como pasta do projeto e, se fornecido, caminho de saida.

NUNCA use outros caminhos para salvar relatorios, arquivos ou manifestos, exceto quando explicitamente fornecido pelo usuario. Nao crie subpastas como `reports` ou `output`.

NUNCA crie arquivos ou pastas que nao estejam especificados nas especificacoes dos agentes.

SIGA EXATAMENTE o padrao de saida abaixo.

```bash
/executar-relatorio-completo-estado-projeto
/executar-relatorio-completo-estado-projeto --pasta-projeto=meu-projeto
/executar-relatorio-completo-estado-projeto --pasta-projeto=meu-projeto --pasta-saida=saida-analise
/executar-relatorio-completo-estado-projeto --pastas-ignorar=venv,node_modules,.git,dist
```

## Instrucoes Negativas

1. Nao modificar codigo.
2. Nao executar upgrades ou migracoes.
3. Nao inventar vulnerabilidades.
4. Nao usar linguagem vaga.
5. Nao usar emojis.
6. Nao estimar tempo.
7. Nao criar pastas de agentes na raiz.
8. Nao criar arquivos/pastas nao autorizados.
9. Nao duplicar relatorios existentes.

## Observacoes

Analise cuidadosamente cada etapa do fluxo e determine instrucoes claras para cada agente concluir sua tarefa. Como coordenador mestre (VOCE), forneca todo o contexto necessario a cada agente. Para isso, leia cada especificacao de agente, entenda passo a passo o que ele deve fazer e repasse entradas, restricoes e caminhos especificos.

Somente o orquestrador mantem o **`MANIFESTO.md`**. Instrua o orquestrador a adicionar uma nova entrada imediatamente apos qualquer agente concluir, registrando titulo do relatorio, caminho absoluto iniciado em `/`, nome do agente e timestamp.

Exemplo: assim que o Relatorio de Arquitetura estiver pronto, o orquestrador DEVE adicionar sua entrada no `MANIFESTO.md` e marcar a tarefa como concluida.
