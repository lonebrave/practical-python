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
