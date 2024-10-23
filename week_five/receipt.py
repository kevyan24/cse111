import csv

def main():
  filename = 'products.csv'
  products_dict = read_dictionary(filename, 0)

  print(products_dict)

  print('Requests Items')

  with open('request.csv', 'rt') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)

    for row in reader:
      product_id = row[0]
      quantity = int(row[1])
      
      if product_id in products_dict:
        product_info = products_dict[product_id]
        print(f'{product_info[0]}: {quantity} @ {product_info[1]}')

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
