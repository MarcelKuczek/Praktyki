import json

import requests
class Product:
    id = 0
    name = "produkt"
    weight = 0

    def __init__(self, id, name, weight):
        self.id = id
        self.name = name
        self. weight = weight

    def toJson(self):
        return json.loads(json.dumps(self.__dict__))

product1 = Product(1, "dishwasher", 30)
product2 = Product(2,"Microvave", 5)
product3 = Product(3, "Heater", 5)

products_list = [product1, product2, product3]


