# /********************************************************
# * Name: Logan Christopher and Taylor Wortham Date Assigned: Oct 3, 2018 *
# * Course: CSE 1284 Sec 11 Date Due: Oct 3, 2018 *
# * *
# * File name: diamonds.py *
# * *
# * This program takes a number from user input and based 
# * off of such, draws a diamond *
# ********************************************************/

from time import sleep
import os

def main():
  userHeight = int(input('Enter the height of the diamond: '))
  count = 1

  def cls():
    os.system('cls' if os.name=='nt' else 'clear')

  def validation(userHeight):
    if userHeight > 0 and userHeight % 2 != 0:
      print('The validated height of the diamond is: ', userHeight)
      return userHeight
    else:
      while userHeight < 0 or userHeight % 2 == 0:
        print('ERROR: The height must be an odd number greater than 0.')
        userHeight = int(input('Please re-enter height: '))
      print('The validated height of the diamond is: ', userHeight)
      return userHeight

  def printStage_1(userHeight, count):
    while count <= userHeight:
      print('*' * count)
      count += 1

  def printStage_2(userHeight, count):
    newHeight = userHeight // 2 + 1
    while count <= newHeight:
      print('* ' * count, end='')
      print(' ' * count)
      count += 1

  def printStage_3(userHeight, count):
    space = userHeight // 2
    while space >= 0:
      # print an asterisk spaced out as many times as the amount returned from space variable, then subtract 1
      print(' ' * space, end='')
      print('* ' * count)
      count += 1
      space -= 1

  def printStage_4(userHeight):
    space = 1
    newHeight = userHeight // 2 
    count = newHeight

    while space <= newHeight:
      print(' ' * space, end='')
      print('* ' * count)
      
      space += 1
      count -= 1

  def printDiamond(userHeight, count):
    printStage_3(userHeight, count)
    printStage_4(userHeight)

  userHeight = validation(userHeight)
  printStage_1(userHeight, count)
  sleep(1)
  cls()
  printStage_2(userHeight, count)
  sleep(1)
  cls()
  printStage_3(userHeight, count)
  sleep(1)
  cls()
  printDiamond(userHeight, count)

main()