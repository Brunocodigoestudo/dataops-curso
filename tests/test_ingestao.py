import duckdb

from src.ingestao import carregar_csvs


def test_carrega_csvs_na_camada_raw(tmp_path, monkeypatch):
    pasta_dados = tmp_path / "data"
    pasta_dados.mkdir()
    (pasta_dados / "clientes.csv").write_text("id_cliente,nome\n1,Ana\n")
    (pasta_dados / "produtos.csv").write_text("id_produto,nome\n10,Caderno\n")
    (pasta_dados / "pedidos.csv").write_text("id_pedido,status\n1,pago\n2,aberto\n")
    monkeypatch.chdir(tmp_path)

    carregar_csvs("teste.duckdb")

    con = duckdb.connect("teste.duckdb")
    assert con.execute("SELECT count(*) FROM raw.pedidos").fetchone()[0] == 2
    con.close()
