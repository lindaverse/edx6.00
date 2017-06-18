balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def monthly_total(balance, annualInterestRate, monthlyPaymentRate):
    monthlyPayment = balance * monthlyPaymentRate
    monthlyInterestRate = annualInterestRate/12
    return (balance - monthlyPayment) * (1+monthlyInterestRate)

for i in range(1, 13):
    balance = monthly_total(balance, annualInterestRate, monthlyPaymentRate)
    #print("month" + " " + str(i) + ": " + str(round(balance, 2)))
print(round(balance, 2))