select
    id_pedido,
    id_cliente,
    id_produto,
    quantidade,
    preco_unitario,
    cast(criado_em as date) as criado_em,
    lower(status) as status
from {{ source('raw', 'pedidos') }}
