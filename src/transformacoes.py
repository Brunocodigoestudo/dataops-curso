def calcular_valor_total(pedidos: list[dict]) -> list[dict]:
    """Adiciona valor_total = quantidade * preco_unitario, ignorando cancelados."""
    return [
        {**p, "valor_total": round(p["quantidade"] * p["preco_unitario"], 2)}
        for p in pedidos
        if p["status"] != "cancelado"
    ]
