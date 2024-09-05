from flask import Flask, jsonify
from data import products_list

app = Flask(__name__)


@app.route('/test', methods = ['GET'])
def get_products_list():
    json_products_list = [product.toJson() for product in products_list]
    return jsonify(json_products_list)

if __name__ == '__main__':
    app.run(debug = True)
    print("test")