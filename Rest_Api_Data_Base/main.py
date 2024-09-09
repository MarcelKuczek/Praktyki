from flask import Flask, jsonify, request, abort
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = ''
app.config["MYSQL_DB"] = 'flask_db'

mysql = MySQL(app)

@app.route('/products', methods=['GET'])
def get_products_list():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    results = cur.fetchall()
    cur.close()

    products = [{'id': = row[0], 'name': = row[1], 'weight': = row[2], 'price': = row[3]} for row in results]
    return jsonify(products)

if __name__ = '__main__':
    app.run(port = 3000, debug = True)