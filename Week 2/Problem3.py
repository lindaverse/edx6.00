balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
lowerBound = balance/12
upperBound = (balance * (1.0 + monthlyInterestRate)**12) / 12
epsilon = 0.01

def balanceAfterYear(balance, monthlyInterestRate, monthlyPayment):
    for _ in range(1, 13):
        afterPayment = balance - monthlyPayment
        balance = afterPayment * (1 + monthlyInterestRate)
    return balance

monthlyPayment = (lowerBound + upperBound) / 2
tempBalance = balance
numGueses = 0

while abs(tempBalance) > epsilon:
    tempBalance = balanceAfterYear(balance, monthlyInterestRate, monthlyPayment)
    if tempBalance > epsilon:
        lowerBound = (lowerBound + upperBound) / 2
    else:
        upperBound = (lowerBound + upperBound) / 2
    monthlyPayment = (lowerBound + upperBound) / 2

    numGueses += 1

#print(numGueses)
print("Lowest payment: " + str(round(monthlyPayment, 2)))
