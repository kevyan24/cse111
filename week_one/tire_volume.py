# Import necessary libraries
import math
from datetime import datetime

# Print a line to separate the section
print('------------------------------------------------------------------------')

# Ask the user for the tire dimensions
w = int(input('Enter the width of the tire in mm (ex 205): '))
a = int(input('Enter the aspect ratio of the tire (ex 60): '))
d = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# Calculate the tire volume
v = (math.pi * (w ** 2) * a) * ((w * a) + (2540 * d)) / 10000000000

# Print the approximate tire volume
print(f'The approximate volume is {v:.2f} liters')

# Print a line to separate the section
print('------------------------------------------------------------------------')

# Ask the user if they want to buy tires with the entered dimensions
buy = input('Do you want to buy tires with the dimensions you entered? (Yes/No): ')

# Get the current date and time
date = datetime.now()

# If the user answers "Yes", ask for the phone number and log the information in the "volumes.txt" file
if buy.lower() == 'yes':
  number = int(input('Enter your phone number: '))

  with open('volumes.txt', 'at') as volumes_file:
    print(f'{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, {number}', file=volumes_file)
    print('------------------------------------------------------------------------')
    print('Thank you for choosing our tires!')

# If the user answers "No", log the information in the "volumes.txt" file without the phone number
else:
  with open('volumes.txt', 'at') as volumes_file:
    print(f'{date:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volumes_file)
  print('------------------------------------------------------------------------')
  print('Goodbye!')