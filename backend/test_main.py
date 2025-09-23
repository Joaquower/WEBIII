import pytest
import mongomock
from fastapi.testclient import TestClient
import main  # important: we need to patch main.collection_historial

client = TestClient(main.app)

# Create mock DB and collection
mongo_client = mongomock.MongoClient()
database = mongo_client.practica1
mock_collection = database.historial


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 2.5, 5.0),
    (1e10, 1e10, 2e10)
])
def test_sum_numbers(monkeypatch, a, b, expected):
    # 🔹 Patch the collection that main.py uses
    monkeypatch.setattr(main, "collection_historial", mock_collection)

    # Clean before test
    mock_collection.delete_many({})

    response = client.get(f"/calculator/sum?a={a}&b={b}")
    
    # ✅ Assert response correctness
    assert response.status_code == 200
    assert response.json() == {"a": a, "b": b, "result": expected}
    
    # ✅ Assert that the record was inserted into mongomock
    saved = mock_collection.find_one({"a": a, "b": b})
    assert saved is not None
    assert saved["result"] == expected

def test_historial(monkeypatch):
    monkeypatch.setattr(main, "collection_historial", fake_collection_historial)
    response= client.get("/calculadora/historial")
    assert response.status_code ==200

    expected_data = list(fake_collection_historial.find({}))
    historial = []
    for document in expected_data:
        historial.append({
            "a": document["a"],
            "b": document["b"],
            "resultado": document["resultado"],
            "date": document["date"].isoformat(),
        })
    
    print(f"DEBUG expected_data: {historial}")
    print(f"DEBUG expected_data: {response.json()}")

    assert response.json() == {"historial":historial}