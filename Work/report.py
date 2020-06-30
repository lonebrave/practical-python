# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = {'name': row[0],
                       'shares': int(row[1]),
                       'price': float(row[2])
                       }
            portfolio.append(holding)

    return portfolio


def read_prices(filename):
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
    basis = 0.0
    current_value = 0.0
    for stock in portfolio:
        basis += stock['shares'] * stock['price']
        current_value += stock['shares'] * prices[stock['name']]

    gain = current_value - basis
    print('Gain is {:0.2f}'.format(gain))


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        change = prices[stock['name']] - stock['price']
        report.append((stock['name'],
                       stock['shares'],
                       stock['price'],
                       change
                       ))

    return report


def main():
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    report = make_report(portfolio, prices)
    for name, shares, price, gain in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {gain:10.2f}')


if __name__ == "__main__":
    main()
