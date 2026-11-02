# Postmortem · status "estornado" quebrou o deploy

Formato blameless: o foco é o sistema que permitiu o erro, não a pessoa.

## O que aconteceu
A origem passou a enviar pedidos com status "estornado". O teste
`accepted_values` de `stg_pedidos` barrou o build, e o `fct_pedidos` não foi
atualizado. Nenhum número errado chegou a quem consome os dados.

## Linha do tempo
- HH:MM o CI falhou no teste `accepted_values` de `stg_pedidos`
- HH:MM issue aberta com a label `incidente`
- HH:MM negócio confirmou: estorno é válido e não entra no faturamento
- HH:MM correção em produção e issue fechada

## Causa raiz
O modelo não previa o status "estornado". Não havia acordo com a origem
avisando sobre novos status.

## O que funcionou
O teste de dados barrou o dado antes do mart. O dashboard não mostrou valor errado.

## Ações
- [x] Aceitar "estornado" como status válido e tirá-lo do faturamento (dbt e Python)
- [x] Novo unit test no dbt: `valor_total_ignora_estornados`
- [x] Novo teste no pytest: `test_remove_pedidos_estornados`
- [ ] Combinar com o time da origem um aviso prévio para novos status
