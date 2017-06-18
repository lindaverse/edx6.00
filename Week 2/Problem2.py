balance = 3329
annualInterestRate = 0.2

import math

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def balanceAfterYear(balance, annualInterestRate, monthlyPayment):
    monthlyInterestRate = annualInterestRate/12
    for i in range(1, 13):
        balance = (balance - monthlyPayment) * (1 + monthlyInterestRate)
    return(balance)

monthlyPayment = roundup(balance/12)-10

tempBalance = balance

while tempBalance > 0:
    tempBalance = balanceAfterYear(balance, annualInterestRate, monthlyPayment)
    if tempBalance > 0:
        monthlyPayment += 10

print(monthlyPayment)
