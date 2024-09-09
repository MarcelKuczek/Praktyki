from flask import Flask, jsonify, abort

from Rest_Api.data import product1
from data import products_list

app = Flask(__name__)


@app.route('/product', methods = ['GET'])
def get_products_list():
    json_products_list = [product.toJson() for product in products_list]
    return jsonify(json_products_list)

@app.route('/product/<int:product_id>', methods = ['GET'])
def get_products(product_id):
    product = next((item for item in products_list if item.id == product_id), None)
    try:
        return jsonify(product.toJson())
    except:
        abort(404)

@app.route('/delete/product/<int:product_id>', methods = ['DELETE'])
def delete_products(product_id):
    try:
        del products_list[product_id]
    except:
        abort(404)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)