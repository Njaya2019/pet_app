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


    def get(self, pet_id):
        cur=self.createCursor()
        if pet_id:
            cur.execute("SELECT * FROM pets WHERE id =%s" % (pet_id))
            pet=cur.fetchone()
            if pet:
                return jsonify({'Pet':pet}), 201 
            else:
                return jsonify({'message':'Pet doesn\'t exist'}), 404
        else:
            cur.execute("SELECT * FROM pets")
            pets=cur.fetchall()
            if not pets:
                return jsonify({'message':'no pets in our records'}), 404
            cur.close()
            return jsonify({'Pets':pets}), 201
            
    
    def post(self):
        

        
        con=self.connectDB()
        cur=con.cursor()
        pet_name=request.json["pet_name"]

        cur.execute("INSERT INTO pets (pet_name) VALUES (%s)", [pet_name])
        
        con.commit()
        return jsonify({'message':'pet created'})

        
