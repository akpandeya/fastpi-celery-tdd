import json
import pytest
from src.main import app
from sqlmodel import create_engine
from fastapi.testclient import TestClient

@pytest.fixture(scope="module")
def client():
    SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db"

    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

    with TestClient(app) as client:
        yield client

    # clean up
    with engine.begin() as conn:
        conn.execute("DELETE FROM orders")
        conn.execute("DELETE FROM order_items")

def test_create_order(client):
    # prepare test data
    order_data = {
        "customer_name": "John Smith",
        "customer_email": "john.smith@example.com",
        "shipping_address": "123 Main St, Anytown USA",
        "payment_info": "4242 4242 4242 4242",
        "items": [
            {
                "product_id": 1,
                "quantity": 2,
                "discount_code": "SPECIAL10"
            },
            {
                "product_id": 2,
                "quantity": 1,
                "discount_code": None
            }
        ]
    }

    # send POST request to create order
    response = client.post("/orders", json=order_data)

    # check response status code
    assert response.status_code == 201

    # check response body
    data = response.json()
    assert data["tracking_number"] is not None
    assert data["total_cost"] == 19.99 + 9.99 * 2 - 2  # should be 36.97 after discount
    assert len(data["items"]) == 2

    # check database record
    with engine.begin() as conn:
        result = conn.execute("SELECT COUNT(*) FROM orders").first()
        assert result[0] == 1

        result = conn.execute("SELECT COUNT(*) FROM order_items").first()
        assert result[0] == 2
