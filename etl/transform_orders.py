from decimal import Decimal
from typing import Sequence


def transform_orders(orders: Sequence[tuple]) -> dict[str, Decimal | int]:
    nb_orders = len(orders)
    somme = Decimal(0)

    for order in orders:
        somme = order[4] + somme

    moyenne = somme / nb_orders if nb_orders > 0 else Decimal(0)   
    return {
        "nb_orders": nb_orders,
        "somme": somme,
        "moyenne": moyenne,
    }


