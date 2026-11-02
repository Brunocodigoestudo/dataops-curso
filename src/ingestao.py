"""Carrega os CSVs da pasta data/ para a camada bruta (raw) do DuckDB."""

import os

import duckdb

# No seu computador usa dataops.duckdb; no CI, a variável DUCKDB_PATH aponta para outro banco
BANCO = os.getenv("DUCKDB_PATH", "dataops.duckdb")
TABELAS = ["clientes", "produtos", "pedidos"]


def carregar_csvs(caminho_banco: str = BANCO) -> None:
    con = duckdb.connect(caminho_banco)
    con.execute("CREATE SCHEMA IF NOT EXISTS raw")
    for tabela in TABELAS:
        con.execute(
            f"CREATE OR REPLACE TABLE raw.{tabela} AS "
            f"SELECT * FROM read_csv_auto('data/{tabela}.csv')"
        )
        total = con.execute(f"SELECT count(*) FROM raw.{tabela}").fetchone()[0]
        print(f"raw.{tabela}: {total} linhas")
    con.close()


if __name__ == "__main__":
    carregar_csvs()
