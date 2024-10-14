def main():
  text_list = read_list('provinces.txt')
  print(text_list)

  remove_element(text_list)

  count = count_provinces(text_list)
  print(f'\nAlberta occurs {count} times in the modified list.')

def read_list(filename):
  code = {
    'AB': 'Alberta',
  }
  text_list = []
  with open(filename, 'rt') as text_file:
    for line in text_file:      
      clean_line = line.strip()
      if clean_line in code:
        text_list.append(code[clean_line])
      else:
        text_list.append(clean_line)
  return text_list

def count_provinces(text_list):
  count = 0
  for item in text_list:
    if item == 'Alberta':
      count += 1
  return count

def remove_element(text_list):
  text_list.remove(text_list[0])
  text_list.remove(text_list[-1])
  return text_list

if __name__ == "__main__":
  main()  