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
def test_get(cli):
    response=cli.get('/petsdb/')
    data=json.loads(response.data)
    assert data=={'Pets':[[ 1,  "Obama"],[2, 'Raila']]}
    assert response.status_code==201
def test_PetAPIdb_get(cli):
    response=cli.get('/petsdb/'+str(1))
    data=json.loads(response.data)
    assert response.status_code==201
    assert data=={'Pet':[1,'Obama']}
def test_get_unavailable_pet(cli):
    response=cli.get('/petsdb/'+str(3))
    data=json.loads(response.data)
    assert response.status_code==404
    assert 'Pet doesn\'t exist' in data["message"]


    
    


   



