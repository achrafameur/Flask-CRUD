from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class CarModel(db.Model):
    __tablename__ = "cars"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    price = db.Column(db.Integer())
    image = db.Column(db.String())
 
    def __init__(self,id,name,price,image):
        self.id=id
        self.name = name
        self.price = price
        self.image = image

    def serialize(self):
        return {
        'id': self.id,
        'name': self.name,
        'price': self.price,
        'image':self.image
        }

    def  __str__(self) -> str:
        return "c'est la voiture"+str(self.name)+" et elle a pour prix"+str(self.price)
