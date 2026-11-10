from typing import Any


def extract_orders(conn: Any) -> list[tuple]:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM commandes;")
        return cur.fetchall()
    

