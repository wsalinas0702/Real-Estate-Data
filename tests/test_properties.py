from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_properties_returns_data():
    response = client.get("/properties")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 3
    assert {"id", "address", "city", "state"}.issubset(data[0].keys())


def test_get_property_success():
    response = client.get("/properties/1")
    assert response.status_code == 200
    result = response.json()
    assert result["id"] == 1
    assert result["city"] == "Austin"


def test_get_property_not_found():
    response = client.get("/properties/999")
    assert response.status_code == 404


def test_market_summary_requires_matching_properties():
    response = client.get("/properties/market-summary", params={"city": "Austin", "state": "TX"})
    assert response.status_code == 200
    summary = response.json()
    assert summary["city"] == "Austin"
    assert summary["inventory_count"] >= 1


def test_market_summary_not_found():
    response = client.get(
        "/properties/market-summary",
        params={"city": "Nowhere", "state": "ZZ"},
    )
    assert response.status_code == 404
