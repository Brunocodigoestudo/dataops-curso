"""Camada fina de I/O: lê do banco, chama a transformação e grava o resultado."""
from src.transformacoes import calcular_valor_total

COLUNAS = ["id", "quantidade", "preco_unitario", "status"]


def carregar_pedidos(con) -> None:
    linhas = con.execute(
        "SELECT id, quantidade, preco_unitario, status FROM raw_pedidos"
    ).fetchall()
    pedidos = [dict(zip(COLUNAS, linha)) for linha in linhas]
    validos = calcular_valor_total(pedidos)

    # CREATE OR REPLACE recria a tabela a cada execução: é isso que torna o pipeline idempotente
    con.execute("CREATE OR REPLACE TABLE fct_pedidos (id INT, valor_total DOUBLE)")
    con.executemany(
        "INSERT INTO fct_pedidos VALUES (?, ?)",
        [(p["id"], p["valor_total"]) for p in validos],
    )
