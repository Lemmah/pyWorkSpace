# Total Charge Calculator
# Created by James Lemayian.
# This program calculates the total charge for an order from an online store in Canada.

# asking for user country and order total.
orderTotal = int(input("What is your order total?: "))
country = input("Which country do you come from?: ")
# setting my flag.
originCanada = False
if country.upper() == "CANADA":
    originCanada = True
# ask for province if canada.
if originCanada:
    province = input("Which is your province: ")
    if province.upper() == "ALBERTA":
        totalCharge = orderTotal + (orderTotal * 0.05)
    elif province.lower() == "ontario" or province.lower() == "new brunswick"\
            or province.lower() == "nova scotia":
        totalCharge = orderTotal + (orderTotal * 0.13)
    else:
        totalCharge = orderTotal + (orderTotal * 0.06) + (orderTotal * 0.05)
else:
    totalCharge = orderTotal
print("\nYour total charge is: {0:0.2f}\n".format(totalCharge))

