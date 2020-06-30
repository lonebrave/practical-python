# pcost.py
#
# Exercise 1.27
import sys
import csv


def portfolio_cost(filename):
    '''
    Takes a filename as input, reads the portfolio data in that file,
    and returns the total cost of the portfolio as a float.
    '''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        headers = next(rows)

        totalcost = 0
        for n, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                totalcost += nshares * price
            except ValueError:
                print(f"Row {n}: Couldn't convert: {row}")

    return totalcost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Total cost: {}'.format(portfolio_cost(filename)))
