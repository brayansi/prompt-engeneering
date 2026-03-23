# Introdução ao Prompt Engineering

## O que é Prompt Engineering

**Prompt Engineering** é a disciplina de projetar, escrever e otimizar os inputs (prompts) usados para interagir com sistemas de IA generativa, em especial com Large Language Models (LLMs). O objetivo é guiar o modelo em direção a respostas que atendam aos requisitos desejados, de forma consistente e previsível.

### Definições de referência

- **IBM**: ajuda modelos de IA generativa a compreenderem melhor as instruções e a responderem às consultas por meio de prompts de alta qualidade — "bons prompts geram bons resultados".
- **OpenAI**: o processo de escrever instruções efetivas para um modelo, de modo que ele gere conteúdo que atenda de forma consistente aos seus requisitos.
- **Google Cloud**: criar prompts que desbloqueiem as capacidades dos LLMs, permitindo que compreendam a intenção, sigam instruções e produzam saídas desejadas — funciona como "um roadmap para a IA".

Em conjunto, essas definições apontam para a mesma ideia: o prompt é a interface principal entre humanos e modelos; a forma como ele é construído determina diretamente a qualidade, relevância e precisão da saída.

### Arte e ciência

O termo combina duas dimensões: **arte** (criatividade, nuance, adaptação ao contexto) e **ciência** (estrutura, reprodutibilidade, técnicas baseadas em evidências). Não se trata apenas de “fazer boas perguntas” de forma intuitiva; envolve conhecimento de técnicas, trade-offs e limitações dos modelos.

### Contexto acadêmico e evolução do campo

O Prompt Engineering é uma área de pesquisa ativa e relativamente recente. O levantamento sistemático *The Prompt Report* (Schulhoff et al., 2024, arXiv:2406.06608) observa que o campo ainda sofre com “terminologia conflitante e entendimento ontológico fragmentado do que constitui um prompt efetivo”. O mesmo trabalho organiza:

- um vocabulário de 33 termos técnicos;
- uma taxonomia de 58 técnicas de prompting para LLMs;
- 40 técnicas para outras modalidades (imagem, áudio, etc.);
- boas práticas e diretrizes para engenharia de prompt.

Essa sistematização indica que o tema está em evolução e que existe base empírica e acadêmica para as práticas que usamos hoje — não são apenas “dicas da internet”.

### Por que isso importa na prática

A diferença na forma como você interage com a IA pode gerar resultados muito diferentes em quantidade e qualidade de informação — como fazer a mesma pergunta para um adolescente e para um pós-doutor. O Prompt Engineering é o conjunto de práticas que nos permite aproximar o segundo cenário.

### Escopo deste material

O conteúdo aqui está focado no contexto de **desenvolvimento de software**, mantendo a mesma linguagem e complexidade do domínio. As técnicas podem variar conforme o domínio (marketing, direito, saúde etc.), mas os princípios permanecem.

## Visão geral dos cenários de aplicação

O Prompt Engineering atua em três frentes principais:

- **Produtividade no desenvolvimento**: uso de prompts como ferramenta de apoio no dia a dia (automação, soluções rápidas, documentação, code review).
- **Desenvolvimento de aplicações com IA**: quando você integra IA na sua aplicação — agentes, sistemas multiagente — e o prompt define comportamento, escopo e limites.
- **Uso como usuário final**: interação com plataformas como ChatGPT, Gemini, Claude e demais ferramentas; a forma de perguntar influencia diretamente a qualidade da resposta.

## Como escolher o foco

Uma regra simples:

- Use **prompts para produtividade** quando quiser ganhar agilidade em tarefas repetitivas ou exploratórias (código, docs, análise).
- Use **Prompt Engineering em aplicações** quando estiver construindo sistemas que dependem de IA; nesse caso, custo, latência e tamanho do prompt passam a pesar diferente.
- Domine **técnicas de prompt** em ambos os cenários para ser mais intencional e obter melhores resultados.

Importante: durante o desenvolvimento, você pode usar prompts longos e ricos em contexto; em aplicações em produção, muitas vezes quanto menor e mais eficiente o prompt, melhor (custo e latência).

## Principais conceitos técnicos

- **Role Prompting**: definição explícita do papel do modelo (ex.: "você é um especialista em desenvolvimento de software"); ajuda a controlar estilo e consistência.
- **Escopo e comportamento**: o prompt define até onde o agente pode atuar e qual o nível de proatividade permitido.
- **Segurança e privacidade**: prompts mal estruturados podem levar a vazamento de dados ou execução de tarefas fora do escopo desejado.
- **Tipos e técnicas de prompt**: diferentes formatos (role, few-shot, chain-of-thought, etc.) influenciam benchmarks e resultados; não existe uma fórmula universal.
- **Modelos menores vs. maiores**: em modelos menores, técnicas como role prompting tendem a ter impacto mais perceptível; em modelos grandes, o contraste pode ser menor.

## Aplicações no desenvolvimento de software

O Prompt Engineering ajuda em praticamente todas as etapas do ciclo de vida do software:

- Desenvolvimento e manutenção de sistemas existentes
- Automação de tarefas repetitivas e soluções rápidas para problemas específicos
- Estruturação de raciocínio para problemas complexos
- Geração de documentação e design docs
- Code review e brainstorming de soluções
- Criação de mensagens de commit
- Condução de agentes de IA especializados em codificação

## Prompt Engineering em aplicações com IA

Quando o software em si utiliza IA, o prompt passa a definir:

- **Comportamento e escopo**: como o sistema deve agir e até onde pode atuar (ex.: cálculo de taxa de juros considerando histórico do cliente).
- **Nível de proatividade**: se a IA deve interpretar necessidades, antecipar ações ou manter-se reativa.
- **Respostas especializadas**: direcionamento para tarefas específicas, com ou sem acesso a dados externos (APIs, bancos de dados).
- **Segurança**: evitar exposição de dados sensíveis (comissões, faturamento, tabelas internas) por meio de prompts mal definidos.
- **Robustez em modelos pequenos**: pequenas alterações no prompt podem quebrar o comportamento; a precisão da instrução é crítica.

## Prompt Engineering como nova linguagem de programação

O prompt passa a ser o "código" que define comportamento em sistemas baseados em IA. Os `if`s e `else`s tradicionais são substituídos, em parte, por decisões probabilísticas da própria IA. O que orienta e limita o agente é, em grande medida, o prompt.

Antes, programava-se em Go, Python ou outra linguagem; hoje, é comum escrever em linguagem natural e gerar código nesses idiomas. O Prompt Engineering é, portanto, parte fundamental dessa nova camada de programação.