from getpass import getpass
from typing import Any

import psycopg

from etl.create_summary import load_summary
from etl.extract_orders import extract_orders
from etl.transform_orders import transform_orders


def run_pipeline(conn: Any) -> dict[str, Any]:
    """Run the complete ETL flow with the caller-provided connection."""
    orders = extract_orders(conn)
    summary = transform_orders(orders)
    load_summary(conn, summary)
    return summary


def _connection() -> psycopg.Connection:
    """Create the single PostgreSQL connection used by the pipeline."""
    password = getpass("Enter your PostgreSQL password: ")
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="delivery_db",
        user="postgres",
        password=password,
    )


def main() -> None:
    # The context manager commits on success, rolls back on error, and closes
    # the one connection after the whole pipeline has finished.
    with _connection() as conn:
        summary = run_pipeline(conn)

    print(
        "Pipeline completed: "
        f"{summary['nbr_commandes']} orders, "
        f"total={summary['somme']}, average={summary['moyenne']}"
    )


if __name__ == "__main__":
    main()
