'''
Create a class called Order which stores item and its price
Use Dunder function __gt__() to convey that:
    order1>order2 if price of order1>price of order2
'''


class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2):
        return self.price>ord2.price


ord1 = Order("Chips",25)
ord2 = Order("Biscuit",50)

print(ord1>ord2)