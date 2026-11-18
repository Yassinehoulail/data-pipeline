from typing import Any


def load_summary(conn: Any, summary: dict[str, Any]) -> None:
    with conn.cursor() as cur:
        # orders_summary has no key column, so replace its single snapshot row.
        # The caller's connection context commits both statements together.
        cur.execute("DELETE FROM orders_summary;")
        cur.execute(
            """
            INSERT INTO orders_summary (nb_orders, somme, moyenne)
            VALUES (%s, %s, %s);
            """,
            (
                summary["nb_orders"],
                summary["somme"],
                summary["moyenne"],
            ),
        )
    
