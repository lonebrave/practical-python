# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    '''
    Takes a filename as input, reads the portfolio data in that file,
    and returns the total cost of the portfolio as a float.
    '''

    with open(filename, 'rt') as f:
        data = f.read()

    mylist = data.split()

    del mylist[0]

    totalcost = 0
    for item in mylist:
        symbol, shares, cost = item.split(',')
        totalcost += float(shares) * float(cost)
    
    return totalcost


print('Total cost: {}'.format(portfolio_cost('Data/portfolio.csv')))
