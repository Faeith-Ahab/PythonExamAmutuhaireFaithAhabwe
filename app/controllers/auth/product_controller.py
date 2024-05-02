from app.status_codes import (
    HTTP_400_BAD_REQUEST,
    HTTP_409_CONFLICT,
    HTTP_201_CREATED,
    HTTP_500_INTERNAL_SERVER_ERROR,
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
)
from flask import Blueprint, request, jsonify

from app.models.product import Product
from app.extensions import db

store = Blueprint('store', __name__, url_prefix='/api/v1/store')


# CREATE A PRODUCT

@store.route('/', methods=['GET'])
def create_product():
    try:
        
        data = request.get_json()

        # Validating input
        required_fields = ['name', 'price', 'description']
        if not all(field in data for field in required_fields):
            return jsonify({"error": "All fields are REQUIRED"}), 400


        
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        

        # Check for existing product with the same name
        existing_product = User.query.filter_by(name=name).first()
        if existing_product:
            return jsonify({'error': 'Product already exists'}), 409 
        
        new_product = Product(
            
            name=name,
            price=price,
            description=description
            
        )  
        
        db.session.add(new_product)
        db.session.commit()

        return jsonify({'message': 'Product added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500




# GET ALL PRODUCTS

@store.route('/products/', methods=('GET',))  
def get_all_products():

    product = Product.query.all()
    output = []
    for product in product:
        product_data = {
            'name': name.id,
            'price': price.id,
            'description': description.id,
            
        }
        output.append(product_data)
    return jsonify({'product': output})




# DELETE A PRODUCT

@store.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete product', 'details': str(e)}), 500




