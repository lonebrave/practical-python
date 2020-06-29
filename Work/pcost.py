# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'rt') as f:
    data = f.read()

mylist = data.split()

del mylist[0]

totalcost = 0
for item in mylist:
    symbol, shares, cost = item.split(',')
    totalcost += float(shares) * float(cost)

print('Total cost: {}'.format(totalcost))
