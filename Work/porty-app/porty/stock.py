from . import typedproperty


class Stock:
    '''
    Class representing a holding of stock.
    '''
    name = typedproperty.String('name')
    shares = typedproperty.Integer('shares')
    price = typedproperty.Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock('{self.name}',{self.shares},{self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares += -shares
