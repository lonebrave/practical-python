# pcost.py
#
# Exercise 1.27
from report import read_portfolio


def portfolio_cost(filename):
    '''
    Takes a filename as input, reads the portfolio data in that file,
    and returns the total cost of the portfolio as a float.
    '''

    portfolio = read_portfolio(filename)

    return portfolio.total_cost


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    print('Total cost: {}'.format(portfolio_cost(filename)))


if __name__ == '__main__':
    import sys
    main(sys.argv)
