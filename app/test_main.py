from fastapi.testclient import TestClient

from app.main import app  # Ensure this correctly points to the FastAPI app instance

client = TestClient(app)

def test_read_main():
    response = client.get("/")  # Ensure this is the correct endpoint you want to test
    assert response.status_code == 200
    assert response.json() == {"msg": "FIN DE LA DEMO DEVOPS"} 

