select
    id_cliente,
    nome,
    cidade
from {{ source('raw', 'clientes') }}
