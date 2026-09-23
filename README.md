# estudos-2027

Diário público do meu ciclo de estudo de setembro de 2026 a setembro de 2027: engenharia de dados, DevOps e cibersegurança, uma hora por dia em cada trilha, de segunda a sexta.

Este repositório é o registro do processo — exercícios, laboratórios, anotações e o que deu errado no caminho. Não é vitrine. Os projetos completos ficam em repositórios próprios, linkados no fim desta página.

---

## Como está organizado

    estudos-2027/
    ├── dados/          # Python, SQL, PySpark, Databricks, Airflow, dbt, AWS, GCP, Scala, Go
    ├── devops/         # Linux, redes, Docker, Kubernetes, Terraform, CI/CD, observabilidade, SRE
    ├── seguranca/      # fundamentos, criptografia, Security+, OWASP, IAM, dados, blue team
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
| 40–42 | Scala | ⏳ |
| 43–45 | Go | ⏳ |
| 46–49 | Projeto final | ⏳ |

### DevOps para SRE

| Módulo | Status |
| --- | --- |
| Linux e shell | 🔄 |
| Redes | ⏳ |
| Docker | ⏳ |
| SLI, SLO e error budget | ⏳ |
| Kubernetes | ⏳ |
| Terraform | ⏳ |
| CI/CD | ⏳ |
| Observabilidade | ⏳ |
| Resposta a incidentes | ⏳ |

### Cibersegurança

| Módulo | Status |
| --- | --- |
| Fundamentos | 🔄 |
| Redes e sistemas | ⏳ |
| Criptografia aplicada | ⏳ |
| Security+ | ⏳ |
| OWASP Top 10 | ⏳ |
| IAM e cloud | ⏳ |
| Segurança de dados e LGPD | ⏳ |
| Blue team e detecção | ⏳ |

Legenda: ✅ concluído · 🔄 em andamento · ⏳ a fazer

---

## Convenções

Commits seguem `trilha/modulo(semana): assunto`:

    dados/python(s01): listas, tuplas e slicing
    devops/linux(s02): journalctl e diagnóstico de serviço
    seguranca/cripto(s04): TLS handshake e erros comuns

Um commit por sessão, no fim da hora de estudo. Dias de teoria também commitam — o que muda é que o conteúdo é a anotação da semana, não código.

Notebooks vão para o repositório sem saída executada.

Nada de credencial, dado de produção ou resultado de scan contra alvo de terceiro. O `.gitignore` cobre os suspeitos de sempre e o secret scanning está ligado, mas a primeira barreira sou eu.

---

## Stack coberto

`Python` `SQL` `PySpark` `Delta Lake` `Databricks` `Airflow` `dbt` `AWS` `GCP` `Scala` `Go` `Docker` `Kubernetes` `Terraform` `GitHub Actions` `Prometheus` `Grafana` `Linux`

---

## Projetos

Os projetos com README próprio, testes e documentação de arquitetura ficam separados:

- _(a preencher)_

---

## Por que público

Porque o registro de um ano de estudo vale mais visível do que guardado, inclusive a parte em que eu não entendi na primeira vez.
