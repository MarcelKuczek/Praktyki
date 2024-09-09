from flask import Flask, jsonify
from data import products_list

app = Flask(__name__)


@app.route('/list', methods = ['GET'])
def get_products_list():
    json_products_list = [product.toJson() for product in products_list]
    return jsonify(json_products_list)

@app.route('/product/<int:product_id>', methods = ['GET'])
def get_products(product_id):
    product = next((item for item in products_list if item.id = product_id), None)
    return jsonify(product)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)