from decimal import Decimal
from typing import Any

import psycopg
from airflow.hooks.base import BaseHook
from airflow.sdk import dag, task


def connect_to_db() -> psycopg.Connection:
    """Create a PostgreSQL connection from the Airflow connection."""
    airflow_conn = BaseHook.get_connection("delivery_postgres")

    return psycopg.connect(
        host=airflow_conn.host,
        port=airflow_conn.port or 5432,
        dbname=airflow_conn.schema,
        user=airflow_conn.login,
        password=airflow_conn.password,
    )


@dag(
    dag_id="delivery_pipeline",
    schedule=None,
    catchup=False,
    tags=["delivery", "etl"],
)
def delivery_pipeline():
    @task
    def extract_pipeline() -> list[list[Any]]:
        from etl.extract_orders import extract_orders

        with connect_to_db() as db_conn:
            orders = extract_orders(db_conn)

        # XCom uses JSON by default. Convert database-specific values before
        # returning the rows to the next task.
        serialized_orders = []
        for order in orders:
            row = list(order)
            row[4] = str(row[4])
            if row[6] is not None:
                row[6] = row[6].isoformat()
            serialized_orders.append(row)

        return serialized_orders

    @task
    def transform(orders: list[list[Any]]) -> dict[str, Any]:
        from etl.transform_orders import transform_orders

        # Restore the numeric amount after the XCom JSON round trip.
        numeric_orders = [
            [*order[:4], Decimal(str(order[4])), *order[5:]]
            for order in orders
        ]
        summary = transform_orders(numeric_orders)

        # Keep the task result JSON-serializable while preserving exact values
        # for PostgreSQL's NUMERIC columns.
        return {
            "nb_orders": summary["nb_orders"],
            "somme": str(summary["somme"]),
            "moyenne": str(summary["moyenne"]),
        }

    @task
    def load(summary: dict[str, Any]) -> None:
        from etl.create_summary import load_summary

        with connect_to_db() as db_conn:
            load_summary(db_conn, summary)

    orders = extract_pipeline()
    summary = transform(orders)
    load(summary)


delivery_pipeline()
