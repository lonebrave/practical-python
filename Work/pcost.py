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

        next(rows)

        totalcost = 0
        for row in rows:
            try:
                totalcost += float(row[1]) * float(row[2])
            except ValueError:
                print('Error converting data. Skipping this item.')

    return totalcost


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print('Total cost: {}'.format(portfolio_cost(filename)))
