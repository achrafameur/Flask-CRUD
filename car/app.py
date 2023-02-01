from flask import Flask, jsonify, request 
from Models import db, CarModel
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@db:3306/lesson'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"Hello": "World"})
    
@app.route("/car", methods=["GET"])
def get_all_car():
    car = CarModel.query.all()
    return jsonify([i.serialize for i in car])
    
@app.route("/car/<id>", methods=["GET"])
def get_car(id):
    car = CarModel.query.get(id)
    return jsonify(car.serialize)

@app.route("/add", methods=["POST"])
def add():
    data = json.loads(request.data) 
    name = data["name"]
    price = data["price"]
    image = data["image"]
    car = CarModel(name=name, price=price, image=image)
    db.session.add(car)
    db.session.commit()
    return jsonify({"message": "Add the car :", "data": data["name"] + data["price"] + data["image"]})

@app.route("/car/<id>", methods=["DELETE"])
def delete(id):
    db.session.query(CarModel).filter_by(id=id).delete()
    db.session.commit()
    return "Element supprimé avec succés"