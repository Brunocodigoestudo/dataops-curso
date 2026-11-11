# Régua de maturidade DataOps

Preenchida na Aula 1 e refeita na última aula. Comparar o antes e o depois é o fio condutor do curso.

## Os níveis

| Dimensão | Nível 1 · Manual | Nível 2 · Repetível | Nível 3 · Automatizado |
| --- | --- | --- | --- |
| Versionamento | Scripts soltos na máquina | Git, mas commits direto na main | Branches, pull request e main protegida |
| Testes | Nenhum, só olho no dashboard | Testes manuais ocasionais | pytest e testes de dados do dbt no CI |
| Deploy | Copiar e colar em produção | Script de deploy manual | GitHub Actions com staging, aprovação e produção |
| Observabilidade | Erro descoberto pelo usuário | Logs conferidos à mão | Dado ruim barrado no CI e métricas DORA |
| Colaboração | Conhecimento em 1 pessoa | Algum README | Code review, padrões, ADR e runbook |

## Avaliação do projeto

| Dimensão | Antes (Aula 1) | Depois (Aula 6) |
| --- | --- | --- |
| Versionamento | 2 · Git, commits direto na main | 3 · Branches, pull request e main protegida |
| Testes | 1 · Nenhum | 3 · pytest e testes de dados do dbt no CI |
| Deploy | 1 · Manual | 3 · GitHub Actions com aprovação |
| Observabilidade | 1 · Erro descoberto pelo usuário | 3 · Dado ruim barrado no CI e métricas DORA |
| Colaboração | 2 · Algum README | 3 · Code review, padrões, ADR e runbook |
