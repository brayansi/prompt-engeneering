---
allowed-tools: Task, Read, Write, TodoWrite
description: Executa um relatorio completo do estado do projeto cobrindo dependencias, arquitetura e componentes.
required-agents: orquestrador, auditor-de-dependencias, analisador-arquitetural, analisador-profundo-de-componentes
---
# Relatorio Completo do Estado do Projeto

## Descricao

Produza uma visao completa e auditavel do projeto coordenando agentes especialistas e consolidando seus resultados. Claude Code (VOCE) atua como coordenador. O agente `orquestrador` prepara estrutura e sintetiza saidas. Entregavel final:

1. Arquivo `README-AAAA-MM-DD-HH:MM:SS.md` com timestamp atual, salvo no diretorio do orquestrador, contendo descricao curta do projeto e indice com links para todos os relatorios.

Ao montar o indice, use titulo + link absoluto iniciado por `/` a partir da raiz do repositorio:

```markdown
[Arquitetura do Projeto](/<caminho-do-relatorio>)
```

Valide todos os links antes de salvar o README. Use o `MANIFESTO.md` do orquestrador como fonte da verdade: inicializado na Fase 1, atualizado nas Fases 2 e 3, finalizado na Fase 4.

## Restricoes Criticas

1. Nunca delegar o fluxo inteiro ao orquestrador.
2. O orquestrador faz apenas:
   - Fase 1: preparar estrutura.
   - Fase 4: sintetizar saidas e finalizar manifesto.
3. Separacao estrita:
   - Cada especialista em uma chamada `Task` separada.
   - O orquestrador nao cria subagentes.
   - VOCE coordena sequencia e paralelismo.
4. Seguir exatamente as especificacoes dos agentes.
5. Nao criar pastas/arquivos fora do que foi definido.
6. Nao fornecer recomendacoes, plano de acao ou alteracoes de codigo.
7. Nao estimar tempo.
8. Nao inventar CVEs.

## Fluxo de Execucao

**Fase 1: `Task(orquestrador)`**
1. Ler flags e normalizar caminhos (`--pasta-projeto`, `--pasta-saida`, `--pastas-ignorar`).
2. Criar somente diretorios exigidos.
3. Aplicar lista de ignorados antes de qualquer leitura.
4. Inicializar `MANIFESTO.md` com estrutura vazia de indice.

**Fase 2: `Task(auditor-de-dependencias)` e `Task(analisador-arquitetural)` em paralelo**
1. Auditor produz relatorio de dependencias.
2. Analisador produz relatorio de arquitetura.
3. A cada conclusao, chamar `Task(orquestrador)` para registrar no `MANIFESTO.md`.

**Fase 3: `Task(analisador-profundo-de-componentes)` em paralelo (um por componente)**
1. Ler relatorio de arquitetura e extrair todos os componentes listados.
2. Disparar uma tarefa por componente.
3. Garantir cobertura de 100% dos componentes.
4. Se faltar componente sem relatorio, disparar tarefas adicionais.
5. Nao duplicar relatorios.

**Fase 4: `Task(orquestrador)`**
1. Consolidar referencias de todos os relatorios.
2. Finalizar `MANIFESTO.md` com validacoes, deduplicacao e checagem de caminhos.

**Fase 5: `Task(VOCE)`**
1. Ler `MANIFESTO.md`.
2. Gerar indice do README com links absolutos validados.
3. Salvar `README-AAAA-MM-DD-HH:MM:SS.md` no diretorio do orquestrador.

## Exemplos de Uso

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

Analise cuidadosamente cada passo e forneca contexto completo para cada agente. O orquestrador e o unico responsavel por manter o `MANIFESTO.md`, registrando titulo, caminho absoluto, nome do agente e timestamp imediatamente apos cada tarefa concluida.
