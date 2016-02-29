# Challenge#4
# * calculate shipping charges for a shopper
# * Ask the user to enter the amount for their total purchase
# * If their total is under $50 add $10, otherwise shipping is free
# * Tell the user their final total including shipping costs and format
#   the number so it looks like a monetary value
# * Don't forget to test your solution with
#     - a value > 50
#     - a value < 50
#     - a value of exactly 50

shopperCash = float(input("Enter Total Amount to Calculate Charges for Shopper: "))

if shopperCash < 50:
    shopperCash += 10
    print("Total Charges = ${0:0.2f}".format(shopperCash))
else:
    print("You don't need to pay for anything. It's all free!")
print("Thank you for shopping!")
