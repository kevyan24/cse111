import csv
import random
from datetime import datetime, timedelta

def main():
  filename = 'products.csv'

  try:
    products_dict = read_dictionary(filename, 0)

    print(f'Inkom Emporium\n')

    with open('request.csv', 'rt') as csv_file:
      reader = csv.reader(csv_file)
      next(reader)

      number_items = 0
      subtotal_price = 0
      purchased_products = []

      for row in reader:
        product_id = row[0]
        quantity = int(row[1])
        
        try:
          product_info = products_dict[product_id]
          print(f'{product_info[0].capitalize()}: {quantity} @ {product_info[1]}')
          price = float(product_info[1]) * quantity
          number_items += quantity
          subtotal_price += price
          purchased_products.append(product_info)
          
        except KeyError as error:
          print(f'Error: unknown product ID in the request.csv file\n{error}')

        sales_tax = subtotal_price * 0.06

    print(f'\nNumber of items: {number_items}')

    print(f'\nSubtotal: {subtotal_price:.2f}')

    print(f'Sales Tax: {sales_tax:.2f}')

    print(f'Total: {subtotal_price + sales_tax:.2f}')

    print('\nThank you for shopping at the Inkom Emporium.')

    current_date = datetime.now()
    print(f'\n{current_date.strftime('%a %b  %e %H:%M:%S %Y')}')

    current_year = current_date.year
    next_year = datetime(current_year + 1, 1, 1)

    days_remaining = (next_year - current_date).days

    print(f"New Year's Sale begins in {days_remaining} days.")

    thirty_days = current_date + timedelta(days=30)
    return_date = thirty_days.replace(hour=21, minute=0, second=0, microsecond=0)

    print(f'Return by: {return_date.strftime("%a %b  %d %H:%M:%S %Y")}')

    if purchased_products:
      random_number = random.choice(range(5, 50, 5))
      coupon_products = random.choice(purchased_products)
      print(f'\nCoupon Product: {coupon_products[0].capitalize()} with a {random_number}% discount.')

  except FileNotFoundError as error:
    print(f'Error: missing file\n{error}')

def read_dictionary(filename, key_column_index):
  """Read the contents of a CSV file into a compound
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
      key_column_index: the index of the column
          to use as the keys in the dictionary.
  Return: a compound dictionary that contains
      the contents of the CSV file.
  """

  with open(filename, 'rt') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)

    products_dictionary = {}
    for row in reader:
      products_dictionary[row[key_column_index]] = row[1:]
    
    return products_dictionary
  
if __name__ == '__main__':
  main()
