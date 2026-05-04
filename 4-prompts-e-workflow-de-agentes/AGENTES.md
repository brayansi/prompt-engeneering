# AGENTES.md

Este arquivo fornece orientacoes para Agentes de IA ao trabalhar neste capitulo do repositorio.

## Visao Geral do Projeto

Este capitulo demonstra fluxos de trabalho baseados em agentes para analise abrangente de projetos por meio de especificacoes em Markdown. Em vez de implementacao por codigo, o foco e descrever papeis, responsabilidades e padroes de coordenacao para gerar relatorios estruturados.

A arquitetura segue um padrao **coordenador + multiagentes especialistas**, em que o Claude Code atua como coordenador mestre.

## Estrutura

```text
4-prompts-e-workflow-de-agentes/
├── agents/
│   ├── orquestrador.md
│   ├── analisador-arquitetural.md
│   ├── analisador-profundo-de-componentes.md
│   └── auditor-de-dependencias.md
└── commands/
    └── executar-relatorio-completo-estado-projeto.md
```

## Especificacoes dos Agentes

### 1. `orquestrador.md`
- Papel: organizar estrutura, validar caminhos e manter `MANIFESTO.md`.
- Responsavel por registrar saidas de especialistas com titulo, caminho absoluto, agente e timestamp.
- Nao cria subagentes.
- Saida: `docs/agents/orquestrador/MANIFESTO.md`.

### 2. `analisador-arquitetural.md`
- Papel: analisar arquitetura em alto nivel.
- Mapeia stack, componentes criticos, padroes e riscos arquiteturais.
- Saida: `docs/agents/analisador-arquitetural/<arquivo>.md`.

### 3. `analisador-profundo-de-componentes.md`
- Papel: analise detalhada por componente.
- Uma execucao por componente (preferencialmente em paralelo).
- Saida: `docs/agents/analisador-profundo-de-componentes/<arquivo>.md`.

### 4. `auditor-de-dependencias.md`
- Papel: auditar dependencias, versoes e seguranca.
- Usa evidencias verificaveis (Context7/Firecrawl/Web) quando disponivel.
- Nao inventa CVEs.
- Saida: `docs/agents/auditor-de-dependencias/<arquivo>.md`.

## Comando Principal

### `executar-relatorio-completo-estado-projeto.md`

Fluxo esperado:
1. `Task(orquestrador)` para inicializar estrutura e manifesto.
2. `Task(auditor-de-dependencias)` e `Task(analisador-arquitetural)` em paralelo.
3. `Task(analisador-profundo-de-componentes)` em paralelo para cada componente mapeado.
4. `Task(orquestrador)` para finalizar `MANIFESTO.md`.
5. Coordenador gera `README-AAAA-MM-DD-HH:MM:SS.md` com indice de relatorios.

## Regras Criticas

1. Separacao estrita de papeis entre agentes.
2. Todos os caminhos devem ser absolutos (iniciando por `/`) ao registrar artefatos.
3. Nao criar pastas nao autorizadas.
4. Nao modificar codigo-fonte do projeto auditado.
5. Garantir cobertura total de componentes listados no relatorio arquitetural.
6. Evitar duplicacao de relatorios.

## Boas Praticas

- Atualizar `MANIFESTO.md` apos cada tarefa concluida.
- Validar existencia dos caminhos antes de consolidar.
- Usar linguagem objetiva e baseada em evidencias.
- Priorizar paralelismo quando nao houver dependencia de dados.
