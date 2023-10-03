import sqlite3


def get_connector():
    return sqlite3.connect("sqlite.db")


def get_product(code_article: str) -> tuple:
    return list(
        get_connector().execute(
            "select * from produits where code_article=?", (code_article,)
        )
    )[0]
