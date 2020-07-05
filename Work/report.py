# report.py
#
# Exercise 2.4
from fileparse import parse_csv
import stock
import tableformat


def read_portfolio(filename):
    '''
    Read the portfolio file and return a portfolio list.
    '''

    with open(filename) as f:
        portdict = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdict]

    return portfolio


def read_prices(filename):
    '''
    Read the prices file and return a prices dictionary.
    '''

    with open(filename) as f:
        prices = dict(parse_csv(f, has_headers=False, types=[str, float]))

    return prices


def calculate_gain(portfolio, prices):
    '''
    Calculate and print the gain based on the portfolio and prices.
    '''

    basis = 0.0
    current_value = 0.0
    for s in portfolio:
        basis += s.shares * s.price
        current_value += s.shares * prices[s.name]

    gain = current_value - basis
    print('Gain is {:0.2f}'.format(gain))


def make_report(portfolio, prices):
    '''
    Generate the report list based on the porfolio and prices.
    '''

    report = []
    for s in portfolio:
        change = prices[s.name] - s.price
        report.append((s.name,
                       s.shares,
                       prices[s.name],
                       change
                       ))

    return report


def print_report(report, formatter):
    '''
    Print a report based on the passed in report list.
    '''

    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, gain in report:
        rowdata = [name, str(shares), f'${price:0.2f}', f'{gain:0.2f}']
        formatter.row(rowdata)

    return


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Read the provided portfolio and prices files and print the report.
    '''

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)

    # formatter = tableformat.TextTableFormatter()
    # formatter = tableformat.CSVTableFormatter()
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)

    return


def main(argv):
    if len(argv) == 3:
        portfolio_filename = argv[1]
        prices_filename = argv[2]
    else:
        portfolio_filename = 'Data/portfolio.csv'
        prices_filename = 'Data/prices.csv'

    portfolio_report(portfolio_filename, prices_filename)


if __name__ == "__main__":
    import sys
    main(sys.argv)
