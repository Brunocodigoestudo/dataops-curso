import duckdb
import pytest

from src.pipeline import carregar_pedidos


@pytest.fixture
def banco():
    con = duckdb.connect(":memory:")          # banco real, mas descartável
    con.execute("CREATE TABLE raw_pedidos (id INT, quantidade INT, preco_unitario DOUBLE, status VARCHAR)")
    con.execute("INSERT INTO raw_pedidos VALUES (1, 2, 10.0, 'pago'), (2, 1, 5.0, 'cancelado')")
    yield con
    con.close()


def test_pipeline_grava_apenas_validos(banco):
    carregar_pedidos(banco)
    linhas = banco.execute("SELECT id, valor_total FROM fct_pedidos").fetchall()
    assert linhas == [(1, 20.0)]


def test_pipeline_e_idempotente(banco):
    carregar_pedidos(banco)
    carregar_pedidos(banco)                   # rodar 2x não pode duplicar
    total = banco.execute("SELECT count(*) FROM fct_pedidos").fetchone()[0]
    assert total == 1
