import random


class Item:
    def __init__(self, name, price, barcode, sup):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.__qtt = 0
        self.__supplier = sup

    def __str__(self):
        return "name: " + self.name + " | price: " + str(self.price)

    def buy(self, qtt):
        self.__qtt = self.__qtt + int(qtt)
    #     sending request to strause

    def sell(self, qtt):
        if self.__qtt - int(qtt) < 0:
            print("OHHHHHHHH NO, no inventory!!!!, dont sell!!!! or buy only ", self.qtt - int(qtt))
        else:
            self.__qtt = self.__qtt - int(qtt)

    def getQtt(self):
        return self.__qtt

products = []
products.append(Item("Bamba", 6, "23423423423423", "osem"))
products.append(Item("Bisly", 7, "23423423w3i8y3", "osem"))
products.append(Item("Tapuchips", 7, "389749388974wr58", "AAAA"))

for product in products:
    product.buy(random.randint(0, 200))

print("------------ stock -----------")
# stock
for product in products:
    print(product.name, product.getQtt())

# products[0].sell(230)
print("------------ stock -----------")
# stock
for product in products:
    product.__qtt = 15
    print(product, product.name, product.getQtt(), product.__qtt)

