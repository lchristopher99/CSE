# Name: Logan Christopher Date Assigned: 11/7/18
#
# Course: CSE 1284 Sec 11 Date Due: 11/7/18
#
# File name: currency_calc.py
#
# Program Description: Program calculates appropriate amount of bills and coins for a user input amount.


# takes the original amount as paramter
def calcCoins(am):
  # rounds the amount to the second decimal place and floor divides by denom amount. assigns to var
  quarters = round(am, 2) // .25
  
  # if above var is divisible by denom, send amount of times divisible and denom type to displayCoins. Subtract amount of denom divided from original amount.
  if quarters != 0:
    displayCoins(int(quarters), 'quarters')
    am = am - (.25 * quarters)
  
  # same functionality as above
  dimes = round(am, 2) // .10
  
  if dimes != 0:
    displayCoins(int(dimes), 'dimes')
    am = am - (.10 * dimes)
  
  nickles = round(am, 2) // .05
  
  if nickles != 0:
    displayCoins(int(nickles), 'nickles')
    am = am - (.05 * nickles)
  
  pennies = round(am, 2) / .01
  
  if pennies != 0:
    displayCoins(int(pennies), 'pennies')

# Takes amount and denom as parameter and prints it out
def displayCoins(x, y):
  print(x, y)

# takes the original amount as paramter
def calcBills(am):
  # rounds the amount to the second decimal place and floor divides by denom amount. assigns to var
  hundred = am // 100

  # if above var is divisible by denom, send amount of times divisible and denom type to displayCoins. Subtract amount of denom divided from original amount.
  if hundred != 0:
    displayBills(int(hundred), 'hundreds')
    am = am - (100 * hundred)

  # same functionality as above
  fifty = am // 50

  if fifty != 0:
    displayBills(int(fifty), 'fifties')
    am = am - (50 * fifty)

  twenty = am // 20

  if twenty != 0:
    displayBills(int(twenty), 'twenties')
    am = am - (20 * twenty)

  ten = am // 10

  if ten != 0:
    displayBills(int(ten), 'tens')
    am = am - (10 * ten)

  five = am // 5

  if five != 0:
    displayBills(int(five), 'fives')
    am = am - (5 * five)
  
  if int(am) != 0:
    displayBills(int(am), 'ones')

# Takes amount and denom as parameter and prints it out
def displayBills(x, y):
  print(x, y)

# Checks string to ensure user input is a number. Returns error and asks user to retry if not
def checkStr():
  while True:
    try:
      am = float(input("Enter a valid price (in decimal) and we'll tell you how much of each bill and coin you'll need to best meet that amount: "))
      return round(am, 2)
    except ValueError:
      print()
      print('Not a valid number!')

  
# Main functions calls to check string first then passes the amount returned to calc bills
def main():
  print('Currency Calculator')
  print()

  am = checkStr()
  calcBills(am)

  # to retrieve decimal amount the amount % 1 returns just the decimal which is then passed to calcCoins
  dec = am % 1
  calcCoins(round(dec, 2))

if __name__ == '__main__':
  main()