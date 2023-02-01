from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class CarModel(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Integer())
    image = db.Column(db.String(512))
    
    def __int__(self, name, price, image):
        self.name = name 
        self.price = price 
        self.image = image 
    
    @property 
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image": self.image
        }