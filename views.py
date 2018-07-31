from flask import Blueprint
from app_db import PetAPIdb


pet_appdb=Blueprint('pet_appdb',__name__)

pet_viewdb=PetAPIdb.as_view('pet_apidb')

pet_appdb.add_url_rule('/petsdb' ,view_func=pet_viewdb, methods=['POST'])
pet_appdb.add_url_rule('/petsdb/', defaults={'pet_id':None} ,view_func=pet_viewdb, methods=['GET'])
pet_appdb.add_url_rule('/petsdb/<int:pet_id>' ,view_func=pet_viewdb, methods=['GET','PUT','DELETE'])

