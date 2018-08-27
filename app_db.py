from flask.views import MethodView
from flask import request, jsonify, abort
import MySQLdb

class PetAPIdb(MethodView):
    def connectDB(self):
        db=MySQLdb.Connect("localhost","root","","pet")
        return db
    def createCursor(self):
        cursor=self.connectDB().cursor()
        return cursor



            
    
    def post(self):
        con=self.connectDB()
        cur=con.cursor()
        pet_name=request.json["pet_name"]

        cur.execute("INSERT INTO pets (pet_name) VALUES (%s)", [pet_name])
        
        con.commit()
        return jsonify({'message':'pet created'})

        
