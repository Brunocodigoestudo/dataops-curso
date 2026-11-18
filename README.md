# dataops-curso

Projeto prático do curso **Engenharia de Dados: DataOps, CI/CD e Liderança Técnica** (Alura), com Bruno Corrêa.

Ao longo das aulas, um pipeline de dados de uma loja (pedidos, clientes e produtos) sai do nível 1 de maturidade, com scripts que funcionam mas sem testes nem automação, e chega a um projeto com testes, CI/CD, padrões de código e métricas.

## Comandos da Aula 5 · Mentoria e liderança técnica

Roteiro da aula: copie um bloco de cada vez (botão de copiar no canto do bloco), cole no terminal do Codespace e confira o resultado.

O vídeo 5.1 é só de slides, sem comandos.

### 5.2 · Os quatro formatos de pair

**1. Atualizar a main e criar a branch.**

```bash
git switch main
git pull
git switch -c docs/documentacao
```

**2. Trazer as descrições dos modelos.** A source, o staging e o mart, cada um com a sua descrição.

```bash
git checkout origin/aula-05-lideranca -- models/staging/_sources.yml models/staging/_staging.yml models/marts/_marts.yml
code models/staging/_sources.yml
code models/staging/_staging.yml
code models/marts/_marts.yml
```

**3. Conferir que nada quebrou.**

```bash
dbt build
```

Resultado esperado: `PASS=11`.

### 5.3 · Knowledge sharing

**1. Gerar e abrir a documentação.** O primeiro comando gera o site da documentação. O segundo abre o site na porta 8080.

```bash
dbt docs generate
dbt docs serve --no-browser
```

Clique em **Open in Browser** no aviso da porta 8080. Veja a descrição do `fct_pedidos` e o grafo de linhagem (botão azul no canto inferior direito). Para parar, volte ao terminal e aperte **Ctrl+C**.

**2. Trazer o runbook e o README.**

```bash
git checkout origin/aula-05-lideranca -- docs/runbooks/pipeline-falhou.md README.md
code docs/runbooks/pipeline-falhou.md
```

**3. Enviar para o GitHub.**

```bash
git add .
git commit -m "docs: documentacao dos modelos e runbook de incidentes"
git push -u origin docs/documentacao
```

**4. Merge e aprovação.** Abra o pull request, espere o check verde, faça o merge e aprove a produção em **Actions → Review deployments**.

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
├── docs/              documentação do time
├── dbt_project.yml
├── profiles.yml
└── requirements.txt
```
