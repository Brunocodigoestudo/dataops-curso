# dataops-curso

Projeto prático do curso **Engenharia de Dados: DataOps, CI/CD e Liderança Técnica** (Alura), com Bruno Corrêa.

Ao longo das aulas, um pipeline de dados de uma loja (pedidos, clientes e produtos) sai do nível 1 de maturidade, com scripts que funcionam mas sem testes nem automação, e chega a um projeto com testes, CI/CD, padrões de código e métricas.

## Como abrir o ambiente

**Pelo navegador, sem instalar nada (recomendado):**

1. Escolha a branch da aula no seletor de branches do GitHub.
2. Clique em **Code → Codespaces → Create codespace**.
3. Espere o ambiente ficar pronto. Python 3.12, dbt, DuckDB e as demais ferramentas são instalados sozinhos.
4. Ao terminar de estudar, pare o codespace (menu Codespaces → Stop) para não gastar a sua cota gratuita.

**No seu computador:** instale Python 3.12 e Git, depois rode:

```bash
python -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
export DBT_PROFILES_DIR=.          # no Windows: $env:DBT_PROFILES_DIR = "."
```

## Primeiros comandos

```bash
python -m src.ingestao   # carrega os CSVs da pasta data/ no DuckDB
dbt run                  # constrói os modelos
```

## Documentação do time

- **Modelos e linhagem:** `dbt docs generate` e depois `dbt docs serve --no-browser`. No codespace, abra a porta 8080.
- **Quando o pipeline falhar:** [docs/runbooks/pipeline-falhou.md](docs/runbooks/pipeline-falhou.md).
- **Decisões técnicas:** [docs/adr/](docs/adr/).
- **Maturidade do projeto:** [docs/maturidade.md](docs/maturidade.md).

## Uma branch por aula

Cada branch guarda o estado do projeto **ao final** da aula. Para acompanhar uma aula, comece pela branch da aula anterior.

| Branch | Estado do projeto |
| --- | --- |
| `aula-01-inicio` | Scripts funcionando, sem testes e sem CI; régua de maturidade preenchida |
| `aula-02-testes` | Testes com pytest, testes de dados do dbt e cobertura |
| `aula-03-ci-cd` | CI em todo pull request e deploy em staging e production com aprovação |
| `aula-04-padroes` | pre-commit, template de pull request, CODEOWNERS e primeiro ADR |
| `aula-05-lideranca` | Documentação dos modelos e runbook de incidentes |
| `aula-06-metricas` | Postmortem, teste novo a partir do incidente e métricas DORA |

## Estrutura

```text
dataops-curso/
├── .devcontainer/          ambiente do Codespaces
├── .github/
│   ├── workflows/          ci.yml · cd.yml
│   ├── pull_request_template.md
│   └── CODEOWNERS
├── data/                   CSVs de origem
├── src/                    ingestao.py · transformacoes.py · pipeline.py
├── tests/                  testes pytest e teste singular do dbt
├── models/                 staging/ · marts/ (dbt)
├── scripts/                deploy.sh · metricas_dora.py
├── docs/                   maturidade · adr/ · runbooks/ · postmortems/
├── .pre-commit-config.yaml
├── .sqlfluff
├── dbt_project.yml
├── profiles.yml
└── requirements.txt
```
