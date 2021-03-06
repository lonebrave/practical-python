# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
extra_payment_start_month = 60
extra_payment_end_month = 108
months = 0

while principal > 0:
    months += 1
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        if payment + extra_payment > principal:
            total_paid += principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - payment - extra_payment
            total_paid = total_paid + payment + extra_payment
    else:
        if payment > principal:
            total_paid += principal
            principal = 0
        else:
            principal = principal * (1+rate/12) - payment
            total_paid = total_paid + payment

    print(f'{months:>3d} ${round(total_paid,2):10.2f}, ${round(principal,2):10.2f}')


print('Total paid', round(total_paid,2), 'over', months, 'months.')
