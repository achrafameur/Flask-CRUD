from flask import Flask, jsonify, request
import os
import db
import car

app = Flask(__name__)
# app.run(host='localhost', port=5000)

if not os.path.isfile('cars.db'):
    db.connect()

@app.route("/", methods=["GET"])
def hello():
    return jsonify({"Hello": "World"}) 

@app.route("/add", methods=['POST'])
def add():
    req_data = request.get_json()
    name = req_data['name']
    price = req_data['price']
    image = req_data['image']
    crs = [c.serialize() for c in db.view()]
    for c in crs:
        if c['name'] == name:
            return jsonify({
                # 'error': '',
                'res': f'Error! car with name {name} is already used !',
                'status': '404'
            })
    cr = car(db.getNewId(), name, price, image)
    print('new car: ', cr.serialize())
    db.insert(cr)
    new_crs = [c.serialize() for c in db.view()]
    print('cars in lib: ', new_crs) 
    return jsonify({
                'res': cr.serialize(),
                'status': '200',
                'msg': 'new car created Successfully!'
            })

@app.route('/all', methods=['GET'])
def getAll():
    content_type = request.headers.get('Content-Type')
    crs = [c.serialize() for c in db.view()]
    if (content_type == 'application/json'):
        carsJson = request.json
        for c in crs:
            if c['id'] == int(carsJson['id']):
                return jsonify({
                    'res': c,
                    'status': '200',
                    'msg': 'Success getting all cars !'
                })
        return jsonify({
            'error': f"Error ! car with id '{carsJson['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    'res': crs,
                    'status': '200',
                    'msg': 'Success getting all cars !'
                })

@app.route('/car/<id>', methods=['GET'])
def getCarById(id):
    req_args = request.view_args
    # print('req_args: ', req_args)
    crs = [c.serialize() for c in db.view()]
    if req_args:
        for c in crs:
            if c['id'] == int(req_args['id']):
                return jsonify({
                    'res': c,
                    'status': '200',
                    'msg': 'Success getting car by ID !'
                })
        return jsonify({
            'error': f"Error ! car with id '{req_args['id']}' not found!",
            'res': '',
            'status': '404'
        })
    else:
        return jsonify({
                    'res': crs,
                    'status': '200',
                    'msg': 'Success getting car by ID!👍😀'
                })

@app.route("/update", methods=['PUT'])
def update():
    req_data = request.get_json()
    name = req_data['name']
    price = req_data['price']
    image = req_data['image']
    the_id = req_data['id']
    crs = [c.serialize() for c in db.view()]
    for c in crs:
        if c['id'] == the_id:
            cr = car(
                the_id, 
                name, 
                price, 
                image
            )
            print('new car: ', cr.serialize())
            db.update(cr)
            new_crs = [c.serialize() for c in db.view()]
            print('cars : ', new_crs)
            return jsonify({
                'res': cr.serialize(),
                'status': '200',
                'msg': f'Success updating the car named {name}!👍😀'
            })        
    return jsonify({
                'res': f'Error ! Failed to update Car with name: {name}!',
                'status': '404'
            })

@app.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    req_args = request.view_args
    print('req_args: ', req_args)
    crs = [c.serialize() for c in db.view()]
    if req_args:
        for c in crs:
            if c['id'] == int(req_args['id']):
                db.delete(c['id'])
                updated_crs = [c.serialize() for c in db.view()]
                print('updated_crs: ', updated_crs)
                return jsonify({
                    'res': updated_crs,
                    'status': '200',
                    'msg': 'Success deleting car by ID!'
                })
    else:
        return jsonify({
            'error': f"Error ! No car ID sent!",
            'res': '',
            'status': '404'
        })

if __name__ == '__main__':
    app.run()