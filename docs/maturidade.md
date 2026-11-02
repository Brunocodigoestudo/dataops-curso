# Régua de maturidade DataOps

Preenchida na Aula 1 e refeita na última aula. Comparar o antes e o depois é o fio condutor do curso.

## Os níveis

| Dimensão | Nível 1 · Manual | Nível 2 · Repetível | Nível 3 · Automatizado | Nível 4 · Otimizado |
| --- | --- | --- | --- | --- |
| Versionamento | Scripts soltos na máquina | Git, mas commits direto na main | Branches + PR obrigatório | Branch protegida, CODEOWNERS |
| Testes | Nenhum, "olho no dashboard" | Testes manuais ocasionais | Unitários + dados no CI | Cobertura alta, contratos de dados |
| Deploy | Copiar e colar em produção | Script de deploy manual | CI/CD a cada merge | Blue/green, feature flags, rollback |
| Infraestrutura | Criada clicando no console | Documentada em wiki | Terraform versionado | IaC aplicado via pipeline |
| Observabilidade | Descobre o erro pelo usuário | Logs manuais | Alertas de falha | Métricas DORA + SLAs de dados |
| Colaboração | Conhecimento na cabeça de 1 pessoa | Algum README | Code review + padrões | Mentoria, pair, ADRs |

## Avaliação do projeto

| Dimensão | Antes (Aula 1) | Depois (Aula 6) |
| --- | --- | --- |
| Versionamento | 2 · Git, commits direto na main | 3 · Branches + PR obrigatório |
| Testes | 1 · Nenhum | 3 · Unitários + dados no CI |
| Deploy | 1 · Manual | 3 · CI/CD a cada merge |
| Infraestrutura | 1 · Nenhuma como código | 1 · Sem mudança |
| Observabilidade | 1 · Descobre o erro pelo usuário | 3 · Falha barrada no CI, com métricas DORA |
| Colaboração | 2 · Algum README | 3 · Code review + padrões, com ADR e runbook |

A infraestrutura continua no nível 1 de propósito: Terraform, deploy blue/green e
feature flags são a próxima etapa.
