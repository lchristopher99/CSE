def get_string():
  string = input('Enter string:')

  return string

def get_file():
  try:
    file_obj = open('morse_code.txt', 'r')
  except Exception as err:
    print(err)
  else:
    return file_obj

def check_file(ch):
  file_obj = get_file()

  for line in file_obj:
    if ch.capitalize() == line[0]:
      return line

def print_morse(text):
  for ch in text:
    char = check_file(ch)
    if char == None:
      print('Character Not Found For: ' + ch)
    else:
      print(char)

def main():
  print('Morse Code Conversion.')
  text = get_string()
  print_morse(text)

if __name__ == '__main__':
  main()