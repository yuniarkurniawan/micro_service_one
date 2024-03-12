from flask import Blueprint, request, jsonify
from models import Products
from database import db
from services import get_all_product, like


products_routes = Blueprint('products_routes', __name__)

@products_routes.route('/list_products', methods=['GET'])
def get_product_list():

    return get_all_product()

@products_routes.route('/<int:id>/like', methods=['POST'])
def update_product_like(id):
    
    print('=====================================')
    return like(product_id=id)
