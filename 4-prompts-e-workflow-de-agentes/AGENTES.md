# AGENTES.md

Este arquivo fornece orientacoes para Agentes de IA ao trabalhar com codigo neste repositorio.

## Visao Geral do Projeto

Este capitulo demonstra fluxos de trabalho baseados em agentes para analise abrangente de projetos por meio de especificacoes especializadas de agentes. Diferente de implementacoes orientadas a codigo, este capitulo utiliza especificacoes em Markdown que definem papeis, responsabilidades e padroes de coordenacao para analise de projetos de software.

O projeto implementa uma **arquitetura multiagente liderada por coordenador**, em que o Claude Code atua como coordenador mestre, orquestrando agentes especialistas que produzem relatorios estruturados sobre arquitetura, componentes e dependencias do projeto.

## Configuracao do Ambiente

**Sem Ambiente Virtual Necessario**:
- Este capitulo nao possui codigo Python nem `requirements.txt`
- Utiliza o sistema nativo de agentes do Claude Code por meio de especificacoes em Markdown
- Todos os agentes sao definidos como arquivos `.md` em `agents/` e `commands/`

**Requisitos de Uso**:
- Claude Code CLI
- Acesso as especificacoes de agentes
- Opcional: servidores MCP para validacao de dependencias (Context7, Firecrawl)

## Estrutura do Projeto

### Layout de Diretorios

```
4-prompts-e-workflow-de-agentes/
├── agents/
│   ├── orquestrador.md                         # Coordenacao e gestao do manifesto
│   ├── analisador-arquitetural.md              # Analise arquitetural de alto nivel
│   ├── analisador-profundo-de-componentes.md   # Analise profunda de componentes individuais
│   └── auditor-de-dependencias.md              # Analise e validacao de dependencias
└── commands/
    └── executar-relatorio-completo-estado-projeto.md  # Orquestracao do fluxo completo
```

### Especificacoes dos Agentes

#### 1. `orquestrador.md`
**Papel**: Orquestrador de Tarefas e Gerenciador de Registro

**Responsabilidades**:
- Inicializa estrutura do projeto e cria `MANIFESTO.md` como fonte unica da verdade
- Registra todas as saidas dos especialistas com titulo, caminho absoluto, nome do agente e timestamp
- Aplica politica de pastas e normalizacao de caminhos
- Garante cobertura de componentes comparando esperado vs real
- Valida e finaliza `MANIFESTO.md`, garantindo integridade

**Restricoes-Chave**:
- **Nunca invoca outros agentes** — apenas o coordenador mestre faz isso
- Mantem separacao estrita de responsabilidades
- Escreve apenas no diretorio designado `docs/agents/orquestrador/`
- Usa caminhos absolutos enraizados em `/` para todas as referencias

**Local de Saida**: `docs/agents/orquestrador/MANIFESTO.md`

#### 2. `analisador-arquitetural.md`
**Papel**: Especialista em Arquitetura de Alto Nivel

**Responsabilidades**:
- Analisa estrutura do projeto e identifica componentes criticos
- Documenta padroes arquiteturais e decisoes de design
- Produz relatorio abrangente de arquitetura
- Lista todos os componentes para analise posterior

**Padrao de Saida**: `docs/agents/analisador-arquitetural/<nome-do-arquivo>.md`

**Secoes-Chave**:
- Visao geral do projeto
- Stack tecnologica
- Lista de componentes criticos (usada na Fase 3)
- Padroes arquiteturais
- Pontos de integracao

#### 3. `analisador-profundo-de-componentes.md`
**Papel**: Especialista em Analise por Componente

**Responsabilidades**:
- Executa analise profunda de componentes individuais
- Uma instancia de agente por componente (execucao paralela)
- Examina detalhes de implementacao, padroes e preocupacoes
- Produz relatorios individuais por componente

**Padrao de Saida**: `docs/agents/analisador-profundo-de-componentes/<nome-componente>-relatorio-AAAA-MM-DD-HH:MM:SS.md`

**Exigencia de Cobertura**: DEVE analisar TODOS os componentes listados no Relatorio de Arquitetura
- Se o Relatorio listar 10 componentes → 10 tarefas paralelas
- Nenhum componente pode ser omitido
- O coordenador verifica 100% de cobertura

#### 4. `auditor-de-dependencias.md`
**Papel**: Especialista em Dependencias e Seguranca

**Responsabilidades**:
- Cataloga todas as dependencias do projeto
- Valida versoes e status de manutencao
- Identifica vulnerabilidades conhecidas (usando MCPs quando disponivel)
- Fornece avaliacao de seguranca baseada em evidencias

**Padrao de Saida**: `docs/agents/auditor-de-dependencias/<nome-do-arquivo>.md`

**Ferramentas de Validacao**:
- Servidor MCP Context7 para consultas de dependencias
- Servidor MCP Firecrawl para validacao de versao
- **Nunca fabrica CVEs** — apenas reporta problemas verificados

### Fluxo do Comando

#### `executar-relatorio-completo-estado-projeto.md`
**Objetivo**: Fluxo completo de analise de projeto com coordenacao multiagente

**Fluxo de Execucao**:

**Fase 1: Task(orquestrador)**
- Ler flags do usuario (`--pasta-projeto`, `--pasta-saida`, `--pastas-ignorar`)
- Normalizar caminhos e criar diretorios necessarios
- Inicializar estrutura vazia de `MANIFESTO.md`

**Fase 2: Agentes especialistas em paralelo**
- `Task(auditor-de-dependencias)` - Gera relatorio de dependencias
- `Task(analisador-arquitetural)` - Gera relatorio de arquitetura
- Ambos executam em paralelo por eficiencia
- Orquestrador atualiza `MANIFESTO.md` apos cada conclusao

**Fase 3: Analise de componentes (paralelo)**
- Parsear Relatorio de Arquitetura para extrair lista de componentes
- Iniciar `Task(analisador-profundo-de-componentes)` para CADA componente em paralelo
- Verificacao de cobertura: DEVE haver relatorio para todo componente
- Orquestrador registra cada relatorio de componente em `MANIFESTO.md`

**Fase 4: Task(orquestrador)**
- Agrega referencias de todos os relatorios
- Finaliza `MANIFESTO.md` com validacao
- Remove duplicidades e confirma integridade

**Fase 5: Geracao do README**
- Ler `MANIFESTO.md` como fonte da verdade
- Construir indice com titulos de relatorio e links absolutos
- Validar todos os links antes de salvar
- Salvar `README-AAAA-MM-DD-HH:MM:SS.md` no diretorio do orquestrador

## Exemplos de Uso

```bash
# Executar workflow no diretorio atual
/executar-relatorio-completo-estado-projeto

# Especificar pasta do projeto
/executar-relatorio-completo-estado-projeto --pasta-projeto=meu-projeto

# Local de saida customizado
/executar-relatorio-completo-estado-projeto --pasta-projeto=meu-projeto --pasta-saida=saida-analise

# Ignorar pastas especificas (sem varredura)
/executar-relatorio-completo-estado-projeto --pastas-ignorar=venv,node_modules,.git,dist
```

**Estrutura de Saida** (com `--pasta-saida`):
```
<pasta-saida>/
├── orquestrador/
│   ├── MANIFESTO.md
│   └── README-2025-01-13-14:30:00.md
├── analisador-arquitetural/
│   └── relatorio-arquitetural.md
├── analisador-profundo-de-componentes/
│   ├── componente-a-relatorio-2025-01-13-14:32:00.md
│   ├── componente-b-relatorio-2025-01-13-14:32:01.md
│   └── ...
└── auditor-de-dependencias/
    └── relatorio-dependencias-2025-01-13-14:31:00.md
```

## Arquitetura e Conceitos-Chave

### Padrao Multiagente Liderado por Coordenador

**Claude Code (VOCE) = Coordenador Mestre**:
- Sequencia fases e gerencia paralelismo
- Invoca cada agente via chamadas `Task()` separadas
- Orquestrador NUNCA cria subagentes
- Toda comunicacao passa pelo coordenador

**Separacao de Agentes**:
```python
# CORRETO: Coordenador invoca agentes
Task(orquestrador)  # Fase 1
Task(analisador-arquitetural)  # Fase 2
Task(auditor-de-dependencias)  # Fase 2 (paralelo)
Task(orquestrador)  # Atualiza MANIFESTO
Task(analisador-profundo-de-componentes, componente="auth")  # Fase 3
Task(analisador-profundo-de-componentes, componente="api")   # Fase 3 (paralelo)
# ...

# ERRADO: Orquestrador criando agentes
# O orquestrador NAO DEVE invocar outros agentes!
```

**`MANIFESTO.md` como Fonte Unica da Verdade**:
- Apenas o orquestrador escreve em `MANIFESTO.md`
- Atualizado apos CADA agente concluir
- Contem:
  - Relatorios rastreados (titulo, caminho absoluto, agente, timestamp)
  - Notas do fluxo (IDs de tarefa, status)
  - Informacoes gerais (pasta do projeto, lista de ignorados)

### Restricoes Criticas

1. **Separacao Estrita de Agentes**:
   - Cada agente invocado com chamada `Task()` separada
   - Orquestrador NUNCA cria subagentes
   - Claude Code coordena sequencia e paralelismo

2. **Politica de Caminhos**:
   - TODOS os caminhos sao absolutos (iniciados em `/`)
   - NUNCA escrever fora dos locais designados
   - NUNCA criar pastas ad-hoc como `reports/` ou `output/`
   - Seguir exatamente as especificacoes dos agentes

3. **Cobertura de Componentes**:
   - DEVE analisar 100% dos componentes do Relatorio de Arquitetura
   - Coordenador valida cobertura antes da Fase 4
   - Iniciar tarefas adicionais para componentes faltantes

4. **Sem Modificacao de Codigo**:
   - Relatorios sao **descritivos, nao prescritivos**
   - NUNCA sugerir edits, refatoracoes ou migracoes
   - NUNCA abrir PRs ou alterar configuracoes
   - Apenas resumir achados

5. **Seguranca Baseada em Evidencias**:
   - NUNCA fabricar CVEs
   - Usar apenas evidencias do auditor de dependencias
   - Citar nomes e versoes exatos de pacotes
   - Evitar linguagem vaga

6. **Sem Duplicacao**:
   - Orquestrador valida antes de registrar
   - NUNCA duplicar relatorios com nomes/timestamps diferentes
   - Se precisar ajustar: editar relatorio existente, nao criar novo

### Modelo de `MANIFESTO.md`

```markdown
# MANIFESTO — <Nome do Projeto>
Gerado em: AAAA-MM-DD-HH:MM:SS
Caminho do Orquestrador: /docs/agents/orquestrador

## Relatorios Rastreados
- Arquitetura do Projeto: /docs/agents/analisador-arquitetural/relatorio-arquitetural.md
- Componentes:
  - Auth Service: /docs/agents/analisador-profundo-de-componentes/auth-relatorio-2025-01-13-14:32:00.md
  - API Gateway: /docs/agents/analisador-profundo-de-componentes/api-relatorio-2025-01-13-14:32:01.md
- Dependencias: /docs/agents/auditor-de-dependencias/relatorio-dependencias.md

## Fluxo
- Task analisador-arquitetural: concluida em 2025-01-13-14:30:00
- Task auditor-de-dependencias: concluida em 2025-01-13-14:30:05
- Task analisador-profundo-de-componentes (auth): concluida em 2025-01-13-14:32:00
- Task analisador-profundo-de-componentes (api): concluida em 2025-01-13-14:32:01

## Informacoes Gerais
- Pasta do projeto: /Users/user/meu-projeto
- Pasta de saida: /Users/user/meu-projeto/saida-analise
- Pastas ignoradas: venv, node_modules, .git
```

### Modelo de README de Saida

```markdown
# <Nome do Projeto> Relatorio Completo do Estado do Projeto

<Descricao curta do projeto>.

Este documento consolida os principais aspectos do projeto como um raio-X abrangente, cobrindo arquitetura, componentes e dependencias.

Gerado em: AAAA-MM-DD HH:MM:SS

## Visao Geral e Arquitetura
[Arquitetura do Projeto](/docs/agents/analisador-arquitetural/relatorio-arquitetural.md)

## Componentes
- [Auth Service](/docs/agents/analisador-profundo-de-componentes/auth-relatorio-2025-01-13-14:32:00.md)
- [API Gateway](/docs/agents/analisador-profundo-de-componentes/api-relatorio-2025-01-13-14:32:01.md)

## Dependencias
[Relatorio de Dependencias](/docs/agents/auditor-de-dependencias/relatorio-dependencias.md)
```

## Boas Praticas

### Para autores de especificacao de agentes

1. **Definicao clara de papel**:
   - Responsabilidade unica por agente
   - Entradas e saidas explicitas
   - Padrao bem definido de local de saida

2. **Comunicacao com coordenador**:
   - Agentes se comunicam APENAS com coordenador
   - Nunca assumir existencia de outros agentes
   - Fornecer saidas estruturadas e previsiveis

3. **Disciplina de caminhos**:
   - Usar caminhos absolutos iniciados em `/`
   - Seguir especificacao do agente exatamente
   - Nunca criar diretorios nao autorizados

### Para designers de workflow

1. **Maximizar paralelismo**:
   - Fase 2: rodar dependencia + arquitetura em paralelo
   - Fase 3: rodar todos os analisadores de componente em paralelo
   - Sincronizar apenas quando houver dependencia de dados

2. **Verificacao de cobertura**:
   - Parsear Relatorio de Arquitetura para lista de componentes
   - Contar tasks iniciadas vs componentes listados
   - Reexecutar para quaisquer relatorios faltantes

3. **Disciplina do MANIFESTO**:
   - Atualizar apos CADA agente concluir
   - Validar existencia dos caminhos antes do registro
   - Verificar duplicidades por assunto e caminho

## Notas Importantes

- **Sem Codigo Python**: este capitulo e dirigido por especificacoes, nao por codigo
- **Claude Code Obrigatorio**: os agentes funcionam no sistema nativo do Claude Code
- **Sem Dependencias**: nao e necessario `pip install` nem ambiente virtual
- **Validacao de Saida**: sempre verificar se caminhos absolutos existem antes de finalizar
- **Execucao Paralela**: aproveitar paralelismo de `Task()` para performance
- **Integridade dos Relatorios**: nunca duplicar relatorios; editar o existente se necessario

## Instrucoes Negativas

**NUNCA**:
- Modificar base de codigo (sem PRs, refatoracoes, mudancas de configuracao)
- Rodar upgrades ou migracoes (sem `npm update`, `go get -u`)
- Inventar CVEs sem evidencia do auditor de dependencias
- Usar linguagem vaga ("provavelmente seguro", "parece ok")
- Incluir emojis ou caracteres estilizados
- Fornecer estimativas de tempo
- Criar pastas de agentes na raiz do repositorio
- Criar arquivos/pastas nao autorizados (`reports/`, `output/`, `tmp/`)
- Duplicar relatorios (editar existente em vez de criar novo)

**SEMPRE**:
- Seguir especificacoes dos agentes exatamente
- Usar caminhos absolutos iniciados em `/`
- Validar 100% de cobertura de componentes
- Atualizar `MANIFESTO.md` apos cada agente
- Verificar caminhos antes de finalizar
- Fornecer apenas achados baseados em evidencias

## Compatibilidade de Versao

- **Claude Code**: versao mais recente com suporte a sistema de agentes
- **Especificacoes de Agente**: formato Markdown seguindo convencoes de frontmatter YAML
- **Servidores MCP** (opcional): Context7 e Firecrawl para validacao aprimorada
