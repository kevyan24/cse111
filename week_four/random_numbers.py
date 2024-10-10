import random 

def main():
  numbers = [16.2, 75.1, 52.3]
  words = []
  print(f'numbers {numbers}')

  append_random_numbers(numbers)
  print(f'numbers {numbers}')

  append_random_numbers(numbers, 3)
  print(f'numbers {numbers}')

  append_random_words(words, 6)
  print(f'words {words}')

def append_random_numbers(number_list, quantity = 1):
  times = 0
  while times < quantity:
    random_number = random.uniform(0, 100)
    number_list.append(round(random_number, 1))  
    times += 1

def append_random_words(words_list, quantity = 1):
  times = 0
  while times < quantity:
    random_word = random.choice(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine'])
    words_list.append(random_word)
    times += 1

if __name__ == "__main__":
  main()