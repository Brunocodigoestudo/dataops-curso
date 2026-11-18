# dataops-curso

Projeto prático do curso **Engenharia de Dados: DataOps, CI/CD e Liderança Técnica** (Alura), com Bruno Corrêa.

Ao longo das aulas, um pipeline de dados de uma loja (pedidos, clientes e produtos) sai do nível 1 de maturidade, com scripts que funcionam mas sem testes nem automação, e chega a um projeto com testes, CI/CD, padrões de código e métricas.

## Comandos da Aula 2 · Testes automatizados

Roteiro da aula: copie um bloco de cada vez (botão de copiar no canto do bloco), cole no terminal do Codespace e confira o resultado. Você começa da branch `aula-01-inicio` e traz os arquivos desta branch com `git checkout`. Na Aula 2 você trabalha direto na `main`.

### 2.1 · A pirâmide de testes

**1. Trazer a regra de negócio e os testes unitários.** Copia só estes arquivos da branch `aula-02-testes` para o seu projeto.

```bash
git checkout origin/aula-02-testes -- src/transformacoes.py tests/__init__.py tests/test_transformacoes.py
```

**2. Ler a regra e os testes.** A regra é uma função pura: recebe uma lista e devolve uma lista. São três testes, e o `parametrize` roda o mesmo teste com vários cenários.

```bash
code src/transformacoes.py
code tests/test_transformacoes.py
```

**3. Rodar os testes.** O `pytest` procura os testes da pasta `tests/` e roda um por um. O `-v` mostra o nome de cada teste.

```bash
pytest -v
```

Resultado esperado: `5 passed`.

**4. Ver o teste falhar, de propósito.** Em `src/transformacoes.py`, troque `round(p["quantidade"] * p["preco_unitario"], 2)` por `p["quantidade"] * p["preco_unitario"]`, salve e rode:

```bash
pytest -v
```

Resultado esperado: `1 failed`, com o valor `0.30000000000000004`. Desfaça com **Ctrl+Z**, salve e rode `pytest -v` de novo: `5 passed`.

### 2.2 · Integração e idempotência

**1. Trazer o pipeline e o teste de integração.** O pipeline lê do banco, aplica a regra e grava o resultado.

```bash
git checkout origin/aula-02-testes -- src/pipeline.py tests/test_integracao.py
code src/pipeline.py
code tests/test_integracao.py
```

**2. Rodar os testes.** A fixture cria um DuckDB em memória: um banco real, mas descartável.

```bash
pytest -v
```

Resultado esperado: `7 passed`.

**3. Ver a idempotência quebrar, de propósito.** Em `src/pipeline.py`, troque `CREATE OR REPLACE TABLE` por `CREATE TABLE IF NOT EXISTS`, salve e rode:

```bash
pytest -v
```

Resultado esperado: `1 failed`, com `assert 2 == 1`. O pedido apareceu duas vezes. Desfaça com **Ctrl+Z**, salve e rode `pytest -v` de novo: `7 passed`.

### 2.3 · Testando dados com dbt

**1. Trazer os testes de dados.** Testes do staging, unit test do mart e o teste singular.

```bash
git checkout origin/aula-02-testes -- models/staging/_staging.yml models/marts/_marts.yml tests/assert_valor_total_positivo.sql
code models/staging/_staging.yml
code models/marts/_marts.yml
code tests/assert_valor_total_positivo.sql
```

**2. Rodar modelos e testes juntos.** O `dbt build` roda os modelos e os testes na ordem do grafo.

```bash
dbt build
```

Resultado esperado: `PASS=11`.

**3. Colocar um dado ruim, de propósito.** Acrescenta um pedido com o id repetido no fim do CSV, carrega de novo e roda o build.

```bash
echo "5,3,10,1,12.50,pago,2026-10-05" >> data/pedidos.csv
python -m src.ingestao
dbt build
```

Resultado esperado: `FAIL` no teste `unique`, `ERROR=1` e `SKIP=3`. O dado ruim foi barrado no staging.

**4. Desfazer.** Volta o CSV ao original, carrega de novo e roda o build.

```bash
git checkout data/pedidos.csv
python -m src.ingestao
dbt build
```

Resultado esperado: `PASS=11`.

### 2.4 · Cobertura de testes

**1. Medir a cobertura.** Mostra quais linhas os testes executaram. Abaixo de 80%, falha.

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

Resultado esperado: `42%` e `FAIL`. A ingestão inteira está sem teste.

**2. Trazer o teste que falta.** O teste da ingestão roda numa pasta temporária, sem tocar nos dados reais.

```bash
git checkout origin/aula-02-testes -- tests/test_ingestao.py
code tests/test_ingestao.py
```

**3. Medir de novo.**

```bash
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

Resultado esperado: `8 passed` e `96%`.

**4. Salvar a aula no Git.** Prepara os arquivos, registra o commit e envia para o GitHub.

```bash
git add .
git commit -m "test: testes unitarios, integracao e dbt"
git push
```

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

## Uma branch por aula

Cada branch guarda o estado do projeto **ao final** da aula. Para acompanhar uma aula, comece pela branch da aula anterior.

| Branch | Estado do projeto |
| --- | --- |
| `aula-01-inicio` | Scripts funcionando, sem testes e sem CI |
| `aula-02-testes` | Testes com pytest, testes de dados do dbt e cobertura |
| `aula-03-ci-cd` | CI em todo pull request e deploy em staging e production com aprovação |
| `aula-04-padroes` | pre-commit, template de pull request, CODEOWNERS e primeiro ADR |
| `aula-05-lideranca` | Documentação dos modelos e runbook de incidentes |
| `aula-06-metricas` | Postmortem, teste novo a partir do incidente e métricas DORA |

## Estrutura

```text
dataops-curso/
├── .devcontainer/     ambiente do Codespaces
├── data/              CSVs de origem
├── src/               ingestão e transformações em Python
├── models/            modelos dbt (staging e marts)
├── dbt_project.yml
├── profiles.yml
└── requirements.txt
```
