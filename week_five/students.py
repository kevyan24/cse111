import csv

def main():
  I_NUMBER_INDEX = 0
  i_number_index = input('Please enter an I-Number: ')
  student_dictionary = read_dictionary('./students.csv', I_NUMBER_INDEX)

  student = find_student(student_dictionary, i_number_index)
  print(student)


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

    student_dictionary = {}
    for row in reader:
      i_number = row[int(key_column_index)]
      name = row[1]
      student_dictionary[i_number] = name

    return student_dictionary

def find_student(student_dictionary, i_number):
  if i_number in student_dictionary:
    return student_dictionary[i_number]
  elif len(i_number) < 9:
    return "Invalid I-Number: too few digits"
  elif len(i_number) > 9:
    return "Invalid I-Number: too many digits"
  else:
    return "Invalid I-Number"
  
if __name__ == "__main__":
  main()
