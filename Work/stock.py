class Stock:
    '''
    Class representing a holding of stock.
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        # print(f'Stock({self.name},{self.shares},{self.price})')
        return f"Stock('{self.name}',{self.shares},{self.price})"

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares += -shares
