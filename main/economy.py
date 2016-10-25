from main.db import *

class Game():
    save = {'savefile':0, 'firsttime': True}
    product_vals = []

    def setDefParams(self):
        for x in range(len(defvalnames)):
            self.save[defvalnames[x]] = defvalvals[x]

    class Product(object):
        def __init__(self, name, price, id):
            self.name = name
            self.price = price
            self.id = id