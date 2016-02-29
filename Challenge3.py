# You Challenge - create a loan calculator
#
# * Have the user enter the loan amount, the interest rate, and the number of years or months for the loan
# * Calculate monthly payments with the following formula
# 		M = L[i(1+i)n] / [(1+i)n-1]
# * M = monthly payment
# * L = Loan Amount
# * i = interest rate (for an interest rate of 5%, i = 0.05)
# * n = number of payments

# ---- Start loan calculator
loanAmount = float(input('Enter Loan Amount: '))
interestRate = float(input('Enter Interest Rate: '))
numberofPayments = int(input('Enter # of Payments(months): '))

dividendPart = loanAmount * (interestRate * ((1 + interestRate) * numberofPayments))
divisorPart = ((1 + interestRate) * (numberofPayments - 1))
quotientM = dividendPart / divisorPart

print("loanAmount: {0:0.2f} interestRate: {1:0.2f} numberofPayments: {2} ".format(loanAmount, interestRate, numberofPayments))

print("dividendPart: {0:0.2f}".format(dividendPart))
print("divisorPart: {0:0.2f}".format(divisorPart))
print("Result of M(monthly payment): {0:0.2f}".format(quotientM))
