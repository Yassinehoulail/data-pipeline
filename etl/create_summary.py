from typing import Any


def load_summary(conn: Any, summary: dict[str, Any]) -> None:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO orders_summary (nb_orders, somme, moyenne)
            VALUES (%s, %s, %s)  
            """,
            (
                summary["nb_orders"],
                summary["somme"],
                summary["moyenne"],
            ),
        )
    
