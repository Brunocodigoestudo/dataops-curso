# dataops-curso

Projeto prático do curso **Engenharia de Dados: DataOps, CI/CD e Liderança Técnica** (Alura), com Bruno Corrêa.

Ao longo das aulas, um pipeline de dados de uma loja (pedidos, clientes e produtos) sai do nível 1 de maturidade, com scripts que funcionam mas sem testes nem automação, e chega a um projeto com testes, CI/CD, padrões de código e métricas.

## Comandos da Aula 6 · Medindo a transformação DataOps

Roteiro da aula: copie um bloco de cada vez (botão de copiar no canto do bloco), cole no terminal do Codespace e confira o resultado.

Antes de começar, no GitHub: **Issues → Labels → New label**, nome `incidente` → **Create label**.

### 6.1 · Postmortem sem culpados

**1. Criar a branch e trazer o CSV com o pedido estornado.**

```bash
git switch main
git pull
git switch -c incidente/estornado
git checkout origin/aula-06-metricas -- data/pedidos.csv
```

**2. Rodar o pipeline.**

```bash
python -m src.ingestao
dbt build
```

Resultado esperado: `6` linhas, `FAIL` no teste `accepted_values` do status, `ERROR=1` e `SKIP=3`. A origem mandou um status novo: `estornado`.

**3. Seguir o runbook: contar os status.** Consulta o banco e conta quantos pedidos existem de cada status.

```bash
python -c "import duckdb; print(duckdb.connect('dataops.duckdb').sql('select status, count(*) from raw.pedidos group by 1'))"
```

Resultado esperado: pago 3, cancelado 1, aberto 1 e estornado 1.

**4. Abrir a issue do incidente.** No GitHub: **Issues → New issue**, título `Status estornado quebrou o build`, label `incidente` → **Submit new issue**.

**5. Trazer a correção, os testes novos e o postmortem.**

```bash
git checkout origin/aula-06-metricas -- models/staging/_staging.yml models/marts/fct_pedidos.sql models/marts/_marts.yml src/transformacoes.py tests/test_transformacoes.py docs/postmortems/2026-11-estornado.md
code docs/postmortems/2026-11-estornado.md
```

**6. Conferir que tudo passa.**

```bash
pytest -v
dbt build
```

Resultado esperado: `9 passed` e `PASS=12`.

**7. Enviar para o GitHub.**

```bash
git add .
git commit -m "fix: status estornado, testes novos e postmortem"
git push -u origin incidente/estornado
```

**8. Publicar e fechar a issue.** Pull request, check verde, merge, aprovação da produção e, por fim, feche a issue do incidente.

### 6.2 · Métricas DORA

**1. Criar a branch e trazer o script.**

```bash
git switch main
git pull
git switch -c metricas/dora
git checkout origin/aula-06-metricas -- scripts/metricas_dora.py
code scripts/metricas_dora.py
```

**2. Apontar para o seu repositório.** Na linha do `REPO`, coloque o nome do seu repositório, no formato `usuario/repositorio`.

**3. Rodar o script.** Busca os dados na API do GitHub e calcula os deploys por semana e o lead time.

```bash
python scripts/metricas_dora.py
```

Com poucas semanas de histórico o número é pequeno. O que importa é acompanhar a tendência.

### 6.3 · Tempo de recuperação (MTTR)

Sem comando novo: no mesmo `scripts/metricas_dora.py`, veja a função `recuperacao_horas`. Depois, no GitHub, abra a issue do estorno e compare com o tempo de recuperação que o script mostrou no terminal.

### 6.4 · A régua, antes e depois

**1. Trazer a régua preenchida e o README final.**

```bash
git checkout origin/aula-06-metricas -- docs/maturidade.md README.md
code docs/maturidade.md
```

**2. Enviar para o GitHub.**

```bash
git add .
git commit -m "feat: metricas DORA e regua refeita"
git push -u origin metricas/dora
```

**3. Publicar.** Pull request, check verde, merge e aprovação da produção.

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
