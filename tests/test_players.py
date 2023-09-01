from fastapi.testclient import TestClient
from main import app

def test_get_players():
    client = TestClient(app)

    response = client.get('/players')

    assert response.status_code == 200
    
def test_get_player_by_id():
    client = TestClient(app)
    player_id_one = {
    "player_id": 1,
    "fname": "Juan Roman",
    "lname": "Riquelme",
    "age": 42,
    "isPlay": False
    }
    response = client.get("/players/1")

    assert response.status_code == 200
    data = response.json()

    assert data == player_id_one
