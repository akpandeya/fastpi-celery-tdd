from uuid import UUID
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Discount:
    code: str
    rate: int


@dataclass
class Product:
    id: UUID
    name: str
    currency: str
    price: Decimal
    discounts: list[Discount]
    description: str
    image: str
    in_stock: int

    @classmethod
    def from_dict(cls, data):
        discount_data = data.pop("discounts", [])
        discount_list = [Discount(**d) for d in discount_data]
        return cls(discounts=discount_list, **data)
