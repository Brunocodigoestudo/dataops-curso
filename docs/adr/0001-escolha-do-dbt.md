# 0001 · Escolha do dbt para a transformação

## Contexto
O projeto precisa transformar os dados brutos de pedidos em tabelas prontas
para análise, com testes e documentação, rodando no computador do aluno sem custo.

## Decisão
Usar dbt-core 1.12 com o adaptador dbt-duckdb, com versões fixadas no
requirements.txt.

## Consequências
- Transformação em SQL versionado, com testes e linhagem nativos.
- Roda local e no CI, sem servidor.
- O dbt 2.0 (set/2026) fica para uma próxima decisão; o 1.12 tem suporte até jul/2027.
