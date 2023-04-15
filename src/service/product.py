from src.service.base import BaseService
from src.model import Product
from uuid import UUID
import requests


class ProductService(BaseService):
    def __init__(self, url) -> None:
        self.url = url

    def get_by_id(self, id: UUID):
        data = self._get(id)

        return Product.from_dict(data)

    def _get(self, id: UUID):
        response = requests.get(f"{self.url}/{id}")
        if response.status_code == 404:
            raise ValueError(f"Invalid product {id=}")

        return response.json()
