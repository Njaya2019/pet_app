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

def test_name(cur):
    cur.execute("SELECT pet_name FROM pets WHERE id= %s" % (1))
    name=cur.fetchone()
    assert name[0]=="Obama"


    


def test_post(cli):
    response=cli.post('/petsdb',data=json.dumps(dict(pet_name="Raila")),content_type="application/json")
    data = json.loads(response.data)
    assert response.status_code==200
    assert "pet created" in data["message"]

def test_get(cli):
    response=cli.get('/petsdb/')
    data=json.loads(response.data)
    assert data=={'Pets':[[ 1,  "Obama"],[2, 'Raila']]}
    assert response.status_code==201

def test_get_pet(cli):
    response=cli.get('/petsdb/1')
    data=json.loads(response.data)
    assert response.status_code==201
    assert data=={'Pet':[1,'Obama']}

def test_get_another_pet(cli):
    response=cli.get('/petsdb/2')
    data=json.loads(response.data)
    assert response.status_code==404
    assert 'Pet doesn\'t exist' in data["message"]

