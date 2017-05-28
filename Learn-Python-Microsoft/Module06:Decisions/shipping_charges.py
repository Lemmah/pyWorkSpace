# Shipping Charges Calculator
# Created by James Lemayian

# setting my shipping charge flag
shipping_charge = False
shipping_charge_value = 10
total_purchase = int(input('Please input your total purchase: '))
# resetting the shipping charge flag and using it.
if int(total_purchase) < 50:
    shipping_charge = True
    total_purchase += shipping_charge_value
if shipping_charge :
    print('You incurred additional $10 for shipping.\nYour total purchase is now ${0:d}.'.format(total_purchase))
else:
    print('You qualify to enjoy free shipping!\nYour total purchase remains ${0:d}.'.format(total_purchase))
