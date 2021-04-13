from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_same_identification_code():
    response = client.post(
        "/api/v1/comparison",
        json={"person_1": { "identification_number": "abc" }, "person_2": { "identification_number": "abc" } },
    )
    assert response.status_code == 200
    assert response.json() == {
        "score": 1.0
    }
