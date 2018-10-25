# Name: Logan Christopher & Chad Caligary Date Assigned: 9-26-18
# Course: CSE 1284 Sec 11 Date Due: 9-26-18 11:59 P.M.
# File name: leap_year.py
#
# Program Description: Program calculates whther years between range is a leap year, common year, or skippable year.

startYear = int(input('Enter start year: '))
endYear = int(input('Enter end year: '))
if endYear < startYear:
  print('End year must be a larger value than start year.')
else: 
  pass

def main(startYear, endYear):
  while startYear <= endYear:
    if len(str(startYear)) == 4:
      divBy4 = startYear % 4
      divBy100 = startYear % 100
      divBy400 = startYear % 400

      if divBy4 != 0:
        # This is a common year.
        pass
      elif divBy100 != 0:
        print(startYear)
      elif divBy400 != 0:
        # This is a common year.
        pass
      else:
        print(startYear)
      startYear = startYear + 1
    else:
      print('Year must be 4 digits.')
      break

main(startYear, endYear)