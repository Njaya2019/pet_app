from flask import Flask

app=Flask(__name__)

from views import pet_appdb

#app.register_blueprint(pet_app)
app.register_blueprint(pet_appdb)

if __name__=='__main__':
    app.run(debug=True)