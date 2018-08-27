import pytest, json
from application import app
from app_db import PetAPIdb
import MySQLdb


@pytest.fixture(scope="module")
def cli():
    client=app.test_client()
    return client

@pytest.fixture(scope="module")
def cur():
    petApi=PetAPIdb()
    con=petApi.connectDB()
    cur=con.cursor()
    yield cur
    cur.close()
    con.close()




def test_post(cli):
    response=cli.post('/petsdb',data=json.dumps(dict(pet_name="Raila")),content_type="application/json")
    data = json.loads(response.data)
    assert response.status_code==200
    assert "pet created" in data["message"]



