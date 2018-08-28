from flask.views import MethodView
from flask import request, jsonify, abort
import MySQLdb
class PetAPIdb(MethodView):

    db=MySQLdb.Connect("localhost","root","","pet")
    cur=db.cursor()
        


    def get(self, pet_id):
        if pet_id:
            self.cur.execute("SELECT * FROM pets WHERE id =%s" % (pet_id))
            pet=self.cur.fetchone()
            if pet:
                return jsonify({'Pet':pet}), 201 
            else:
                return jsonify({'message':'Pet doesn\'t exist'}), 404
        else:
            self.cur.execute("SELECT * FROM pets")
            pets=self.cur.fetchall()   
            return jsonify({'Pets':pets}), 201

    def post(self):
        cur=self.cur
        pet_name=request.json["pet_name"]
        cur.execute("INSERT INTO pets (pet_name) VALUES (%s)", [pet_name])
        self.db.commit()
        return jsonify({'message':'pet created'})

        
