"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
"""
from datetime import datetime

day = datetime.now().weekday()

prices = float()
price = None
subtotal = float()

print('Enter the price and quantity for each item.')

while price != 0:
  price = float(input('\nPlease enter the price: $'))
  if price == 0:
    print('Thank you for shopping.\n')

  else:
    quantity = float(input("Please enter the quantity: "))

    prices = price * quantity

    subtotal += prices
  
print(f'Subtotal: {subtotal:.2f}')

if subtotal >= 50 and day == 1 or day == 3:
  discount = subtotal * 0.10
  subtotal -= discount
  tax = subtotal * 0.06
  total = subtotal + tax
  print(f'Discount amount: {discount:.2f}')
  print(f'Sales tax amount: {tax:.2f}')
  print(f'Total: {total:.2f}')

elif subtotal < 50 and day == 1 or day == 3:
  tax = subtotal * 0.06
  total = subtotal + tax
  almost_discount = 50 - subtotal
  print(f'To receive the discount, add {almost_discount:.2f} to your order.')
  print(f'Sales tax amount: {tax:.2f}')
  print(f'Total: {total:.2f}')

else:
  tax = subtotal * 0.06
  total = subtotal + tax
  print(f'Sales tax amount: {tax:.2f}')
  print(f'Total: {total:.2f}')


