# report.py
#
# Exercise 2.4
import csv
import sys


def read_portfolio(filename):
    '''
    Read the portfolio file and return a portfolio list.
    '''

    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            holding = {'name': record['name'],
                       'shares': int(record['shares']),
                       'price': float(record['price'])
                       }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
    '''
    Read the prices file and return a prices dictionary.
    '''

    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


def calculate_gain(portfolio, prices):
    '''
    Calculate and print the gain based on the portfolio and prices.
    '''

    basis = 0.0
    current_value = 0.0
    for stock in portfolio:
        basis += stock['shares'] * stock['price']
        current_value += stock['shares'] * prices[stock['name']]

    gain = current_value - basis
    print('Gain is {:0.2f}'.format(gain))


def make_report(portfolio, prices):
    '''
    Generate the report list based on the porfolio and prices.
    '''

    report = []
    for stock in portfolio:
        change = prices[stock['name']] - stock['price']
        report.append((stock['name'],
                       stock['shares'],
                       prices[stock['name']],
                       change
                       ))

    return report


def print_report(report):
    '''
    Print a report based on the passed in report list.
    '''

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(*headers))
    print('-'*10, '-'*10, '-'*10, '-'*10)
    for name, shares, price, gain in report:
        price = f'${price:.2f}'
        print(f'{name:>10s} {shares:>10d} {price:>10s} {gain:10.2f}')

    return


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Read the provided portfolio and prices files and print the report.
    '''

    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report(portfolio, prices)
    print_report(report)

    return


def main():
    if len(sys.argv) == 2:
        portfolio_filename = sys.argv[1]
    else:
        portfolio_filename = 'Data/portfolio.csv'

    prices_filename = 'Data/prices.csv'

    portfolio_report(portfolio_filename, prices_filename)


if __name__ == "__main__":
    main()
