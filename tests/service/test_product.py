import pytest
from src.service import ProductService
from src.model import Product, Discount

PRODUCT_SERVICE_TEST_URL = "http://product-service:8080/product"


def test_get_valid_product():
    product_service = ProductService(url=PRODUCT_SERVICE_TEST_URL)

    id = "9d4f4aa2-4efb-4be6-8e99-294e9730a7b1"

    product = product_service.get_by_id(id)
    assert isinstance(product, Product)
    assert product.id == id

    for discount in product.discounts:
        assert isinstance(discount, Discount)


def test_get_invalid_product():
    product_service = ProductService(url=PRODUCT_SERVICE_TEST_URL)
    with pytest.raises(ValueError) as e:
        product_service.get_by_id("invalid_id")
    assert "Invalid product id" in str(e.value)
