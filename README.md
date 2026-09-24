# estudos-2027

Diário público do meu ciclo de estudo de setembro de 2026 a setembro de 2027: engenharia de dados, DevOps, cibersegurança e engenharia de IA. Uma hora por dia em cada trilha de segunda a sexta, mais quatro horas de IA no fim de semana.

Este repositório é o registro do processo — exercícios, laboratórios, anotações e o que deu errado no caminho. Não é vitrine. Os projetos completos ficam em repositórios próprios, linkados no fim desta página.

---

## Como está organizado

    estudos-2027/
    ├── dados/          # Python, SQL, PySpark, Databricks, Airflow, dbt, AWS, GCP, streaming, modelagem
    ├── devops/         # Linux, redes, Docker, Kubernetes, Terraform, CI/CD, observabilidade, SRE
    ├── seguranca/      # fundamentos, criptografia, Security+, OWASP, IAM, dados, blue team
    ├── ia/             # LLM, RAG, agentes, MCP, avaliação, produção, Mosaic AI
    └── dados-brutos/   # o mesmo conjunto de dados usado o ano inteiro

Dentro de cada trilha há uma pasta por módulo e, dentro dela, uma por semana. Cada semana tem um `README.md` com três seções: **o que aprendi**, **o que não entendi** e **onde continuo**.

A seção "o que não entendi" é proposital. É a parte mais útil do repositório para mim, e a mais honesta para quem estiver lendo.

---

## Progresso

### Engenharia de dados — 49 semanas

| Semanas | Módulo | Status |
| --- | --- | --- |
| 1–6 | Python | 🔄 |
| 7–12 | SQL | ⏳ |
| 13–18 | PySpark | ⏳ |
| 19–23 | Databricks | ⏳ |
| 24–27 | Airflow | ⏳ |
| 28–30 | dbt | ⏳ |
| 31–34 | AWS | ⏳ |
| 35–37 | GCP | ⏳ |
| 38–39 | Qualidade de dados | ⏳ |
| 40–42 | Streaming: Kafka e Spark | ⏳ |
| 43–44 | Modelagem analítica | ⏳ |
| 45 | System design de dados | ⏳ |
| 46–49 | Projeto final | ⏳ |

### DevOps para SRE — 49 semanas

| Semanas | Módulo | Status |
| --- | --- | --- |
| 1–3 | Linux e shell | 🔄 |
| 4 | Redes | ⏳ |
| 5–6 | Docker | ⏳ |
| 7 | SLI, SLO e error budget | ⏳ |
| 9–10 | Kubernetes | ⏳ |
| 11–13 | Observabilidade e incidentes | ⏳ |
| 14–17 | Terraform | ⏳ |
| 18–21 | CI/CD | ⏳ |
| 22–25 | Kubernetes avançado e GitOps | ⏳ |
| 27–30 | Cloud e custo | ⏳ |
| 31–39 | Observabilidade avançada e SRE | ⏳ |
| 40–43 | Segurança da esteira | ⏳ |
| 44–49 | Engenharia de plataforma | ⏳ |

### Cibersegurança — 49 semanas

| Semanas | Módulo | Status |
| --- | --- | --- |
| 1–3 | Fundamentos | 🔄 |
| 4–6 | Criptografia e redes | ⏳ |
| 7–13 | IAM, dados e detecção | ⏳ |
| 14–21 | Security+ | ⏳ |
| 22–26 | OWASP e AppSec | ⏳ |
| 27–30 | Cloud e containers | ⏳ |
| 31–34 | Segurança de dados e LGPD | ⏳ |
| 35–39 | Governança e continuidade | ⏳ |
| 40–43 | Blue team e SOC | ⏳ |
| 44–49 | Threat modeling e relatório | ⏳ |

### Engenharia de IA — 50 fins de semana

| Fins de semana | Módulo | Status |
| --- | --- | --- |
| 1–5 | LLM na prática | 🔄 |
| 6–8 | Transformers e attention | ⏳ |
| 9–15 | Embeddings e RAG | ⏳ |
| 16–23 | Agentes: LangGraph, Agno, CrewAI | ⏳ |
| 24–25 | MCP e protocolos de agente | ⏳ |
| 26–29 | Avaliação e observabilidade | ⏳ |
| 30–37 | IA em produção | ⏳ |
| 38–41 | Mosaic AI no Databricks | ⏳ |
| 42–45 | Segurança e governança em IA | ⏳ |
| 46–50 | Projeto final | ⏳ |

Legenda: ✅ concluído · 🔄 em andamento · ⏳ a fazer

---

## Convenções

Commits seguem `trilha/modulo(semana): assunto`:

    dados/python(s01): listas, tuplas e slicing
    devops/linux(s02): journalctl e diagnóstico de serviço
    seguranca/cripto(s04): TLS handshake e erros comuns
    ia/rag(f11): primeiro RAG com LangChain

Um commit por sessão, no fim da hora de estudo. Dias de teoria também commitam — o que muda é que o conteúdo é a anotação da semana, não código.

Notebooks vão para o repositório sem saída executada.

Nada de credencial, dado de produção ou resultado de scan contra alvo de terceiro. O `.gitignore` cobre os suspeitos de sempre e o secret scanning está ligado, mas a primeira barreira sou eu.

---

## Stack coberto

`Python` `SQL` `PySpark` `Delta Lake` `Databricks` `Airflow` `dbt` `Kafka` `AWS` `GCP` `Docker` `Kubernetes` `Terraform` `ArgoCD` `GitHub Actions` `Prometheus` `Grafana` `Linux` `LangChain` `LangGraph` `MCP` `MLflow` `FastAPI`

---

## Projetos

Os projetos com README próprio, testes e documentação de arquitetura ficam separados:

- _(a preencher)_

---

## Por que público

Porque o registro de um ano de estudo vale mais visível do que guardado, inclusive a parte em que eu não entendi na primeira vez.
