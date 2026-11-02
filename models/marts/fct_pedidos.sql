select
    id_pedido,
    id_cliente,
    criado_em,
    round(quantidade * preco_unitario, 2) as valor_total
from {{ ref('stg_pedidos') }}
where status not in ('cancelado', 'estornado')
