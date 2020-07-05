# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio


def portfolio_cost(filename):
    '''
    Takes a filename as input, reads the portfolio data in that file,
    and returns the total cost of the portfolio as a float.
    '''

    portfolio = read_portfolio(filename)

    totalcost = 0
    for row in portfolio:
        totalcost += row['shares'] * row['price']

    return totalcost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Total cost: {}'.format(portfolio_cost(filename)))
