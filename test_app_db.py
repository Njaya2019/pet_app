import pytest, json
from application import app
from app_db import PetAPIdb
import MySQLdb
@pytest.fixture(scope="module")
def cli():
    client=app.test_client()
    return client
def test_post(cli):
    response=cli.post('/petsdb',data=json.dumps(dict(pet_name="Raila")),content_type="application/json")
    data = json.loads(response.data)
    assert "pet created" in data["message"]



