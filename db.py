import sqlite3,random
from models import car

def getNewId():
    return random.getrandbits(28)
cars = [
    {
        'name': 'Car1',
        'price': 10000,
        'image': 'https://img.freepik.com/premium-photo/generic-brandless-modern-sport-car_110488-1758.jpg?w=2000'
    },
    {
         'name': 'Car2',
        'price': 20000,
        'image': 'https://img.freepik.com/premium-photo/generic-brandless-modern-sport-car_110488-1758.jpg?w=2000'
    },
    {
         'name': 'Car3',
        'price': 30000,
        'image': 'https://img.freepik.com/premium-photo/generic-brandless-modern-sport-car_110488-1758.jpg?w=2000'
    },
    {
        'name': 'Car4',
        'price': 40000,
        'image': 'https://img.freepik.com/premium-photo/generic-brandless-modern-sport-car_110488-1758.jpg?w=2000'
    },
    {
         'name': 'Car5',
        'price': 50000,
        'image': 'https://img.freepik.com/premium-photo/generic-brandless-modern-sport-car_110488-1758.jpg?w=2000'
    },
]    

def connect():
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY, name STRING, price INTEGER, image STRING)")
    conn.commit()
    conn.close()
    for i in cars:
        cr = car(getNewId(),i['name'], i['price'], i['image'])
        insert(cr)

def insert(car):
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO cars VALUES (?,?,?,?)", (
        car.id,
        car.name,
        car.price,
        car.image
    ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM cars")
    rows = cur.fetchall()
    cars = []
    for i in rows:
        crs = car(i[0], True if i[1] == 1 else False, i[2])
        cars.append(crs)
    conn.close()
    return cars

def update(car):
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("UPDATE car SET price=?, name=? WHERE id=?", (car.price, car.name, car.id))
    conn.commit()
    conn.close()

def delete(theId):
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM cars WHERE id=?", (theId,))
    conn.commit()
    conn.close()

def deleteAll():
    conn = sqlite3.connect('cars.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM cars")
    conn.commit()
    conn.close()