from flask.views import MethodView
from flask import request, jsonify, abort
import MySQLdb

class PetAPIdb(MethodView):
   



            
    
    def post(self):
        
        db=MySQLdb.Connect("localhost","root","","pet")
        cur=db.cursor()
        pet_name=request.json["pet_name"]

        cur.execute("INSERT INTO pets (pet_name) VALUES (%s)", [pet_name])
        
        db.commit()
        return jsonify({'message':'pet created'})

        
