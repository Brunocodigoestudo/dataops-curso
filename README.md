# dataops-curso

Projeto prático do curso **Engenharia de Dados: DataOps, CI/CD e Liderança Técnica** (Alura), com Bruno Corrêa.

Ao longo das aulas, um pipeline de dados de uma loja (pedidos, clientes e produtos) sai do nível 1 de maturidade, com scripts que funcionam mas sem testes nem automação, e chega a um projeto com testes, CI/CD, padrões de código e métricas.

## Comandos da Aula 1 · Princípios de DataOps

Roteiro da aula: copie um bloco de cada vez (botão de copiar no canto do bloco), cole no terminal do Codespace e confira o resultado. O comando `code` abre o arquivo no editor.

### 1.4 · O ambiente no Codespaces

**1. Criar o ambiente.** No GitHub, escolha a branch `aula-01-inicio` e clique em **Code → Codespaces → Create codespace**. Espere o terminal aparecer.

**2. Ver a receita do ambiente.** Mostra a imagem com Python 3.12, o comando que instala as dependências e a variável que faz o dbt achar o `profiles.yml`.

```bash
code .devcontainer/devcontainer.json
```

**3. Ver as versões fixadas.** Cada ferramenta tem a versão travada, para todo mundo ter o mesmo resultado.

```bash
code requirements.txt
```

**4. Conferir as versões instaladas.** Mostra a versão do Python e do dbt que o ambiente instalou.

```bash
python --version
dbt --version
```

Resultado esperado: `Python 3.12` e `dbt 1.12.6`. Se aparecer um aviso de versão mais nova, tudo bem: a versão foi fixada de propósito.

**5. Ao terminar de estudar.** Pare o codespace no menu **Codespaces → Stop**, para não gastar a cota gratuita.

### 1.5 · Régua de maturidade

**1. Ver a origem dos dados.** Três clientes, três produtos e cinco pedidos, com status pago, aberto e cancelado.

```bash
code data/pedidos.csv
```

**2. Ver a ingestão.** O script que lê cada CSV e grava na camada `raw` do DuckDB.

```bash
code src/ingestao.py
```

**3. Ver o staging.** Padroniza os dados: converte a data e deixa o status em minúsculo.

```bash
code models/staging/stg_pedidos.sql
```

**4. Ver a regra de negócio.** Valor total é quantidade vezes preço, e pedido cancelado não entra no faturamento.

```bash
code models/marts/fct_pedidos.sql
```

**5. Rodar o pipeline.** O primeiro comando carrega os CSVs no banco. O segundo constrói os modelos do dbt.

```bash
python -m src.ingestao
dbt run
```

Resultado esperado: `3`, `3` e `5` linhas carregadas, e `PASS=3` no dbt. O pipeline funciona.

**6. Avaliar na régua.** A avaliação é feita nos slides da aula: volte para a apresentação.

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
