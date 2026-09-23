# Detecção de fraude: da análise à esteira de produção

Prova técnica para Engenheiro(a) de Analytics Pleno(a) — Serasa Experian.

Cinco entregas: uma arquitetura de feature store híbrida, uma query SQL que evita uma armadilha
de granularidade, uma análise exploratória que encontrou um viés estrutural no dataset, uma
esteira de CI/CD executada num workspace Databricks real, e um DAG de orquestração.

---

![Arquitetura da feature store híbrida](docs/arquitetura.svg)

---

## O que foi entregue

| | Entrega | Resultado |
|---|---|---|
| **1** | [Arquitetura + Data Contract](desafio1/) | Feature store híbrida com separação por volatilidade; contrato em YAML validado no CI |
| **2** | [SQL — HackerRank *Interviews*](desafio2/) | Solução com CTEs, acompanhada de script que demonstra o bug da versão ingênua |
| **3** | [Análise exploratória](desafio3/) | Viés amostral identificado; PR-AUC de 0,830 → 0,972 com feature engineering |
| **4** | [CI/CD com Databricks Asset Bundles](desafio4/) | Executado de ponta a ponta em workspace real, com paridade de resultados confirmada |
| **5** | [Pipeline orquestrado](desafio5/) | DAG na TaskFlow API, com tratamento de falha diferenciado por tipo de erro |

A explicação de cada decisão técnica e das alternativas descartadas está em
[`docs/DOCUMENTACAO_TECNICA.md`](docs/DOCUMENTACAO_TECNICA.md).

---

## O achado que mudou toda a análise

A taxa de fraude por mês deu **100% de fevereiro a novembro**. Isso é absurdo, e investigar o
porquê acabou condicionando todas as decisões seguintes.

A primeira hipótese, erro de parsing de data, foi descartada: o primeiro componente ultrapassa
12 em 70% das linhas e o segundo nunca ultrapassa, então o formato é `dd-mm-yyyy` sem
ambiguidade.

A segunda se confirmou. As transações legítimas existem **apenas** em janeiro de 2019 e
dezembro de 2020 — zero legítimas nos outros 22 meses — enquanto as fraudes cobrem o período
inteiro. O arquivo é uma amostra construída, não um recorte temporal contínuo.

| Período | Transações | Fraudes | Legítimas |
|---|---:|---:|---:|
| 2019-01 | 6.701 | 99 | 6.602 |
| 2019-02 a 2020-11 | 1.625 | 1.625 | **0** |
| 2020-12 | 6.057 | 58 | 5.999 |

Três consequências práticas:

- A taxa global de 12,4% **não é a prevalência real**. Dentro das janelas completas ela fica em
  1,48% e 0,96% — patamar coerente com fraude de cartão em produção.
- Qualquer feature derivada de mês ou ano **vazaria o rótulo** com precisão quase perfeita. Foram
  deliberadamente excluídas.
- A validação **não pode usar split temporal**, porque as classes não coexistem nos mesmos
  períodos. Usei validação cruzada estratificada.

Uma EDA de checklist — `describe()`, `isnull().sum()`, `value_counts()` no target — passaria
direto disso, e o modelo resultante teria performance excelente em validação pela razão errada.

---

## Os sinais que o dataset carrega

![Padrões de valor e temporais](desafio3/outputs/02_padroes_valor_temporais.png)

**Valor.** A mediana da fraude é 7,7× a da legítima (R$ 356 contra R$ 46), concentrada entre
R$ 200 e R$ 900 — nem baixa demais para compensar, nem alta o bastante para disparar bloqueio.
O maior valor da base, aliás, é de uma transação **legítima**: um corte simples do tipo "acima
de X é fraude" não funcionaria.

**Horário.** A janela das 22h às 03h concentra **86% das fraudes com 31% do volume**. Faz
sentido operacionalmente: é o período de menor monitoramento e menor chance de o titular
perceber a transação.

**Segmento.** Os três primeiros colocados têm taxa quase idêntica, mas tickets muito diferentes
— priorizar apenas por taxa esconde a diferença de perda financeira.

| Segmento | Taxa de fraude | Ticket médio da fraude | Perda no período |
|---|---:|---:|---:|
| `shopping_net` | 27,4% | R$ 1.001 | R$ 381.430 |
| `grocery_pos` | 27,2% | R$ 315 | R$ 136.494 |
| `misc_net` | 26,6% | R$ 797 | R$ 172.984 |
| `shopping_pos` | 13,9% | R$ 886 | R$ 165.743 |
| `gas_transport` | 10,7% | R$ 13 | R$ 1.935 |

---

## Feature engineering com ganho medido

Propor features sem medir o efeito é argumentação, não engenharia. Cada uma foi avaliada por
validação cruzada estratificada, usando PR-AUC — e não ROC-AUC, que é otimista em base
desbalanceada porque incorpora a taxa de verdadeiros negativos.

| Conjunto de features | PR-AUC |
|---|---:|
| Apenas `amt` | 0,830 |
| `amt` + `idade` | 0,882 |
| **+ features propostas** | **0,972** |

**`amt_z_categoria`** — z-score do valor dentro da categoria. R$ 300 num posto de gasolina é
anômalo; R$ 300 numa compra online não é. Normalizar por categoria separa o efeito do valor do
efeito do mix de categorias.

**`razao_amt_media_cliente`** — razão entre o valor e a média das transações **anteriores** do
mesmo cliente. Fraude por tomada de conta se manifesta como quebra do padrão individual, e só a
linha de base pessoal captura isso.

O `.shift()` no cálculo dessa segunda feature é o detalhe crítico: sem ele, a média incluiria a
própria transação e a feature carregaria informação do presente para dentro de si mesma — o
modelo ficaria ótimo em validação e medíocre em produção. Há um
[teste dedicado](desafio4/tests/test_transformacoes.py) que quebra se alguém remover o shift.

**Um resultado negativo.** A distância haversine entre cliente e estabelecimento é o sinal
clássico da literatura. Nesta base não discrimina: 75,9 km contra 75,6 km entre as classes. Foi
mantida no código e reportada como tal — descartar uma hipótese com evidência também é
resultado.

---

## Da análise ao pipeline

![Pipeline implementado](docs/pipeline.svg)

O bundle define o job como código: três tasks encadeadas por `depends_on`, com dois targets que
promovem o mesmo artefato entre ambientes trocando apenas configuração.

| | dev | prod |
|---|---|---|
| Nome do job | `[dev] fraud_pipeline` | `fraud_pipeline` |
| Catálogo | `dev_analytics` | `prod_analytics` |
| Compute | single node | autoscale 2–8 |
| Agendamento | pausado | 05:00 diário |
| Executado por | usuário | service principal |
| Faixa do quality gate | 0,01% – 50% | 0,1% – 20% |

A faixa larga em dev é intencional: amostra pequena oscila muito, e um gate apertado ali
produziria falha de teste, não falha real — o que treina o time a ignorar o alerta.

**Os limites do gate são parâmetros no nível do job, não variáveis do bundle.** A distinção
importa: variável de bundle é resolvida em tempo de deploy; parâmetro de job, em tempo de
execução. É o que permite sobrescrever o intervalo na chamada, sem redeploy e sem tocar no
código:

```
databricks bundle run fraud_pipeline --params taxa_fraude_max=0.05
→ [FAIL] taxa_fraude_no_intervalo: 12.3896% (intervalo aceito: 0.10% a 5.00%)
```

Quando o gate reprova, `sys.exit(1)` derruba a task, que derruba o job, que faz o `bundle run`
devolver código diferente de zero, que falha o step do GitHub Actions. A exigência de "falhar o
pipeline se o job falhar" é atendida por propagação natural, sem verificação adicional.

---

## A armadilha do desafio 2

A questão parece ser sobre múltiplos JOINs. O ponto real é granularidade: `View_Stats` e
`Submission_Stats` têm várias linhas por `challenge_id`, e juntá-las diretamente produz um
produto cartesiano.

O que torna o erro perigoso é que ele é **silencioso** — a query roda, não dá erro, e devolve
números plausíveis. Por isso escrevi um script que executa as duas versões lado a lado:

| contest | Com CTEs | Ingênua |
|---|---:|---:|
| 66406 (Rose) | 175 submissões · 156 views | **350 · 312** |
| 66556 (Angela) | 25 · 11 | 25 · 11 |
| 94828 (Frank) | 30 · 41 | 30 · 41 |

Tudo dobrado, e apenas no contest que tem múltiplas linhas de estatística — o que confirma que
a causa é a granularidade, e não um erro geral da query.

---

## Quatro princípios que atravessam as entregas

**Uma implementação por regra de negócio.** As transformações vivem em
[`desafio3/src/transformacoes.py`](desafio3/src/transformacoes.py) e são importadas pela EDA,
pelos testes e pelo DAG do Airflow. A versão PySpark existe porque o Databricks roda Spark — e
a evidência de que estão em paridade é que a execução no workspace deu exatamente os mesmos
números da execução local: 14.383 registros, 12,3896%.

**Limites são configuração, nunca constantes.** O intervalo do quality gate é parâmetro em todos
os pontos: parâmetro de job no Databricks, Airflow Variable no DAG, argumento de função nos
módulos.

**Falhar visivelmente em vez de degradar em silêncio.** Arquivo vazio derruba a ingestão;
registro corrompido vai para quarentena com o motivo registrado; gate reprovado propaga o código
de saída até o workflow. O modo de falha mais caro num pipeline de dados é o que produz números
plausíveis e errados.

**Saber quando não repetir.** No DAG, arquivo de origem ausente levanta `AirflowFailException` e
falha sem retry — um arquivo ausente não vira presente na segunda tentativa. Já o gate levanta
exceção comum, com retry, porque a reprovação pode decorrer de ingestão parcial.

---

## Limitações conhecidas

Registradas porque conhecer os limites do próprio trabalho é parte da entrega.

- **O `id_cliente` é um proxy.** O dataset não traz número de cartão, então derivei de latitude,
  longitude e data de nascimento. São 187 chaves com ~77 transações cada, coerente com uma base
  de portadores — mas dois clientes no mesmo endereço com a mesma data de nascimento colidiriam.
- **A prevalência real é estimada, não observada.** As taxas de 1,48% e 0,96% vêm das duas
  janelas completas; se elas foram escolhidas por critério não aleatório, a estimativa é
  enviesada.
- **Os números de PR-AUC não se transferem para produção.** Em produção o modelo enfrentaria ~1%
  de fraude, não 12%, e a precisão em top-k seria substancialmente diferente.
- **As implementações pandas e PySpark são verificadas por comportamento, não por equivalência
  formal.** Num projeto real, eu acrescentaria um teste que roda as duas sobre o mesmo dado e
  compara linha a linha.
- **Os SLAs da arquitetura são alvos plausíveis, não medidos.** Números reais dependeriam de
  teste de carga com o volume efetivo.

---

## Reproduzir

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python desafio3/eda_fraude.py                    # EDA completa, gera os gráficos
python desafio2/validar_interviews.py            # demonstra o bug de fan-out
pytest desafio4/tests/ -q                        # 25 testes
python scripts/validar_contrato.py desafio1/data_contract_qtd_transacoes_24h.yaml
```

Python 3.10+. O notebook `desafio3/eda_fraude.ipynb` já vem com as saídas gravadas.

Instruções de deploy no Databricks e de execução local do Airflow estão nos READMEs de
[`desafio4/`](desafio4/) e [`desafio5/`](desafio5/).

<details>
<summary>Estrutura do repositório</summary>

```
├── docs/
│   ├── DOCUMENTACAO_TECNICA.md     # decisões técnicas e alternativas descartadas
│   ├── arquitetura.svg
│   └── pipeline.svg
├── scripts/validar_contrato.py     # validador do data contract, roda no CI
├── desafio1/
│   ├── ARQUITETURA.md
│   └── data_contract_qtd_transacoes_24h.yaml
├── desafio2/
│   ├── interviews.sql
│   └── validar_interviews.py
├── desafio3/
│   ├── eda_fraude.py               # fonte única da análise (jupytext)
│   ├── eda_fraude.ipynb            # notebook gerado e executado
│   ├── src/transformacoes.py       # limpeza + feature engineering
│   ├── src/qualidade.py            # regras do quality gate
│   └── outputs/                    # gráficos e artefatos
├── desafio4/
│   ├── databricks.yml              # bundle com targets dev e prod
│   ├── free-edition/               # variante serverless, validada em workspace real
│   ├── src/{ingestao,transformacao,quality_gate}.py
│   └── tests/test_transformacoes.py
├── desafio5/
│   ├── dags/fraud_pipeline_dag.py
│   └── docker-compose.yml
└── .github/workflows/{ci,deploy}.yml
```

</details>
