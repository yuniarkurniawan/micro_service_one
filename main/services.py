from collections import OrderedDict
from flask import make_response, jsonify, abort
from models import Products, ProductsUser
from database import db
import requests
from producer import publish

def get_all_product():
    try:
        data_product = db.session.query(Products).all()
        return jsonify(data_product)

    except Exception as e:
        dict_json_response = OrderedDict()
        dict_json_response['message'] = e
        dict_json_response['code'] = 400
        return make_response(jsonify(dict_json_response), 400)
    
def like(product_id:int):
    
    req = requests.get('http://localhost:8000/api/users')
    data_json = req.json()

    try:
        product_user = ProductsUser(
            user_id = data_json['id'],
            product_id = product_id
        )

        db.session.add(product_user)
        db.session.commit()


        publish('product_liked', product_id)
    except Exception as e:
        abort(400, 'Anda telah menekan tombol like')

    return jsonify({
        'message': 'Succes'
    })

    