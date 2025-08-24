import pytest
from app.main import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Test the /hello endpoint."""
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}
