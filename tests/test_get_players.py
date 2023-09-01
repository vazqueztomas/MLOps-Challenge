from fastapi.testclient import TestClient
from main import app
from routes import players

def test_get_players():
    client = TestClient(app)

    response = client.get('/players')

    assert response.status_code == 200
    data = response.json()
    
