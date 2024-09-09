from idlelib.rpc import request_queue

from flask import Flask, jsonify, request, abort
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'market'

mysql = MySQL(app)

@app.route('/products', methods=['GET'])
def get_products_list():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    results = cur.fetchall()
    cur.close()

    products = [{'id': row[0], 'name': row[1], 'weight': row[2], 'price': row[3]} for row in results]
    return jsonify(products)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products WHERE id = %s', (product_id,))
    result = cur.fetchone()
    cur.close()

    if result:
        products = [{'id': result[0], 'name': result[1], 'weight': result[2], 'price': result[3]}]
        return jsonify(products)
    else:
        abort(404)

@app.route('/product', methods=['POST'])
def add_product():
    if not request.json or 'name' in request.json or 'weight' in request.json or 'price' in request.json:
       abort(404)

    data = request.json
    name = data['name']
    weight = data['weight']
    price = data['price']

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO products(name,weight,price)  VALUES (%s, %s, %s)', (name, weight, price))
    mysql.connection.cursor()
    cur.close()

    return jsonify({'message:': 'Product added successfully'}), 201

if __name__ == '__main__':
    app.run(port = 3000, debug = True)