-- teste singular: passa quando a consulta volta zero linha
select
    id_pedido,
    valor_total
from {{ ref('fct_pedidos') }}
where valor_total < 0
