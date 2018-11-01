# Name: Logan Christopher Date Assigned: 10/31/18
#
# Course: CSE 1284 Sec 11 Date Due: 10/31/18
#
# File name: baby_names.py
#
# Program Description: Program opens a list of popular baby names and ranks a user inputed name against the US most popular names.


### Be sure baby_names.py and baby_names folder are within same enclosing folder


def main():
  # searches through files and checks for match between user input name and list name
  def find_name(name, gender, file_name): 
    open_file = list(open(file_name, 'r'))
  
    year = open_file[0].split()[4]

    if file_name == 'baby_names/baby_names_2010s.txt':
      year_ten = open_file[0].split()[5] + 's'

    open_file = iter(open_file)
    for i in range(4):
      next(open_file)

    if file_name == 'baby_names/baby_names_2010s.txt':
      for line in open_file:
        if gender == 'm':
          if name.capitalize() == line.split()[1]:
            return line.split()[0], year_ten
        elif gender == 'f':
          if name.capitalize() == line.split()[3]:
            return line.split()[0], year_ten
    else:
      for line in open_file:
        if gender == 'm':
          if name.capitalize() == line.split()[1]:
            return line.split()[0], year
        elif gender == 'f':
          if name.capitalize() == line.split()[3]:
            return line.split()[0], year
      
  # Checks whther name entered is a double name and if so, executes seperate functions in order to get results for both names
  def dub_name(first, last, file_name):
    if type(file_name) is list:
      for fn in file_name:
        if first and last:
          try:
            rank, year = find_name(first, gender, fn)
            print(year + ' Rank: ' + rank + ' ' + first.capitalize())
            rank, year = find_name(last, gender, fn)
            print(year + ' Rank: ' + rank + ' ' + last.capitalize())
          except:
            print('No Results Found')
        else:
          try:
            rank, year = find_name(first, gender, fn)
            print(year + ' Rank: ' + rank)
          except:
            print('No Results Found')
    else:
      if first and last:
        try:
          rank, year = find_name(first, gender, file_name)
          print(year + ' Rank: ' + rank + ' ' + first.capitalize())
          rank, year = find_name(last, gender, file_name)
          print(year + ' Rank: ' + rank + ' ' + last.capitalize())
        except:
          print('No Results Found')
      else:
        try:
          rank, year = find_name(first, gender, fn)
          print(year + ' Rank: ' + rank)
        except:
          print('No Results Found')

  # splits entered name if double name and later on sends first and last names to dub_check
  def split_name(baby_name):
    if ' ' in baby_name:
      first, last = baby_name.split()
      return first, last
    else:
      first = baby_name
      last = None
      return first, last

  # validates gender entered
  def val_gender(gender):
    while True:
      if gender == 'm' or gender == 'f':
        break
      else:
        print('Please enter valid gender.')
        gender = input('Enter the gender of the baby (m/f):')

  # validates file entered
  def val_file():
    while True:
      file_name = input('Please enter the file name (with extension):')

      try:
        if file_name == 'bonus':
          year_list = ['baby_names/baby_names_1950s.txt', 'baby_names/baby_names_1960s.txt', 'baby_names/baby_names_1970s.txt', 'baby_names/baby_names_1980s.txt', 'baby_names/baby_names_1990s.txt', 'baby_names/baby_names_2000s.txt', 'baby_names/baby_names_2010s.txt']
          return True, year_list
        else:
          open(file_name)
          return True, file_name
      except FileNotFoundError:
        print('File Not Found. Try Again.')

  # starts program by validating file entered by user
  val, file_name = val_file()

  # if file is validated, continue with program
  if val:
    baby_name = input('Enter baby name:')
    gender = input('Enter the gender of the baby (m/f):')

    val_gender(gender)
    first, last = split_name(baby_name)
    dub_name(first, last, file_name)      
    
# executes main function
main()