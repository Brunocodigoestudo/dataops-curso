import pytest

from src.transformacoes import calcular_valor_total


def test_calcula_valor_total():
    pedidos = [{"quantidade": 2, "preco_unitario": 10.5, "status": "pago"}]
    resultado = calcular_valor_total(pedidos)
    assert resultado[0]["valor_total"] == 21.0


def test_remove_pedidos_cancelados():
    pedidos = [{"quantidade": 1, "preco_unitario": 5, "status": "cancelado"}]
    assert calcular_valor_total(pedidos) == []


def test_remove_pedidos_estornados():
    # teste nascido do postmortem docs/postmortems/2026-11-estornado.md
    pedidos = [{"quantidade": 1, "preco_unitario": 89.9, "status": "estornado"}]
    assert calcular_valor_total(pedidos) == []


@pytest.mark.parametrize(
    "qtd, preco, esperado",
    [
        (1, 0.1, 0.1),
        (3, 0.1, 0.3),  # sem o round, 3 * 0.1 daria 0.30000000000000004
        (0, 99.9, 0.0),
    ],
)
def test_valores_de_borda(qtd, preco, esperado):
    pedidos = [{"quantidade": qtd, "preco_unitario": preco, "status": "pago"}]
    assert calcular_valor_total(pedidos)[0]["valor_total"] == esperado
