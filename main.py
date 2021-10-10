from logging import error
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../Day-66(first RESTful API)/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api_key ="TopSecretAPIKey"

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        #The getattr() method returns the value of the named attribute of an object.
        # If not found, it returns the default value provided to the function.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
#By default every route has GET method so you dont need to write
@app.route("/random")
def random_cafe():
    all_cafes=Cafe.query.all()
    print(all_cafes)
    random_cafe=random.choice(all_cafes)
    return jsonify(cafes= { "name" : random_cafe.name,
             "map_url" : random_cafe.map_url ,   
             "img_url" : random_cafe.img_url,
             "location" : random_cafe.location,
             "seats" : random_cafe.seats,
             "has_toilet" : random_cafe.has_toilet,
             "has_wifi" : random_cafe.has_wifi,
             "has_sockets" :random_cafe.has_sockets,
             "can_take_calls": random_cafe.can_take_calls,
             "coffee_price" : random_cafe.coffee_price}
    )

@app.route("/all")
def all_cafes():
    all_cafes=Cafe.query.all()
    cafe_lst=[cafe.to_dict()  for cafe in all_cafes]
             
    return jsonify(cafes=cafe_lst)         

@app.route("/search")
def search_cafe():
    loc=request.args.get("location")
    all_cafes=Cafe.query.filter_by(location=loc).all()
    cafe_lst=[cafe.to_dict()  for cafe in all_cafes]
    return jsonify(cafes=cafe_lst)  


## HTTP POST - Create Record
@app.route("/add",methods=["POST"])
def add_cafe():
   if api_key ==request.args.get("api-key"): 
    if request.method=="POST":
         new_cafe=Cafe( 
                        name = request.form.get("name"),
                        map_url = request.form.get("map_url"),
                        img_url = request.form.get("img_url"),
                        location = request.form.get("location"),
                        seats = request.form.get("seats"),
                        has_toilet =bool(request.form.get("has_toilet")),
                        has_wifi =bool(request.form.get("has_wifi")),
                        has_sockets = bool(request.form.get("has_sockets")),
                        can_take_calls=bool(request.form.get("can_take_calls")),
                        coffee_price =request.form.get("coffee_price") 
                        )
         db.session.add(new_cafe)
         db.session.commit()
         return jsonify(response={"success":"Successfully added a new cafe"})
   else:
        return  jsonify(error={"Not Authorised":"makes sure you have correct api-key"})  


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def update_price(cafe_id):
    if api_key ==request.args.get("api-key"):
      cafe_price_update=Cafe.query.get(cafe_id)
      if cafe_price_update:
        cafe_price_update.coffee_price=request.form.get("coffee_new_price")
        db.session.commit()
        return  jsonify(response={"success":"Successfully updated price"})
      else:
          return  jsonify(error={"Not Found":"Sorry a cafe with that id was not found in the database"})  
    else:
        return  jsonify(error={"Not Authorised":"makes sure you have correct api-key"})  


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>",methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_to_delete=Cafe.query.get(cafe_id)
    if api_key ==request.args.get("api-key"):
       if cafe_to_delete:
           db.session.delete(cafe_to_delete)
           db.session.commit()
           return  jsonify(response={"success":"Successfully deleted Cafe"})
       else:
           return  jsonify(error={"Not Found":"Sorry a cafe with that id was not found in the database"})  
    else:
        return  jsonify(error={"Not Authorised":"makes sure you have correct api-key"})  


if __name__ == '__main__':
    app.run(debug=True)
