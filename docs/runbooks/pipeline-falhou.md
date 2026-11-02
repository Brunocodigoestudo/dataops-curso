# Runbook · o pipeline falhou

Passo a passo para quem estiver de plantão quando o CI ou o deploy ficar vermelho.

## 1. Descubra onde falhou

Abra a aba **Actions** do repositório e entre na execução vermelha. Veja qual step falhou:

| Step que falhou | O que costuma ser | Próximo passo |
| --- | --- | --- |
| Padrões (pre-commit) | Formatação, lint de Python ou de SQL | Rode `pre-commit run --all-files` e faça commit do que ele corrigir |
| Testes unitários e de integração | Mudança de código quebrou uma regra | Rode `pytest` e leia o teste que falhou |
| Build e testes do dbt | Um teste de dados falhou | Vá para o passo 2 |
| deploy-staging ou deploy-producao | Mesmo caso do dbt, no banco do ambiente | Vá para o passo 2 |

## 2. Se foi um teste de dados

Testes de dados falham quando **o dado mudou**, mesmo sem ninguém mexer no código.

1. No log, procure a linha com `FAIL` e o nome do teste (por exemplo, `accepted_values_stg_pedidos_status`).
2. Reproduza no codespace:

```bash
python -m src.ingestao
dbt build --select stg_pedidos
```

3. Descubra o que chegou de diferente. Exemplo para o teste de status:

```bash
python -c "import duckdb; print(duckdb.connect('dataops.duckdb').sql('select status, count(*) from raw.pedidos group by 1'))"
```

## 3. Registre o incidente

1. Abra uma issue com a label `incidente`. A hora de abertura é o "detectado" das métricas.
2. Decida com o time de negócio se o dado novo é válido ou é um erro da origem.
3. Corrija, abra o PR e feche a issue quando a correção estiver em produção.
4. Escreva o postmortem em `docs/postmortems/`. Toda causa raiz vira pelo menos um teste novo.
