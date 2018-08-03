import pytest, json
from application import app
from app_db import PetAPIdb


@pytest.fixture
def cli():
    client=app.test_client()
    return client

def test_post(cli):
    response=cli.post('/petsdb',data=json.dumps(dict(pet_name="Raila")),content_type="application/json")
    data = json.loads(response.data)
    assert response.status_code==200
    assert "pet created" in data["message"]

def test_get(cli):
    response=cli.get('/petsdb/')
    code=response.status_code
    data=json.loads(response.data)
    if code==404:
        assert "no pets in our records" in data["message"]
    assert response.status_code==201


