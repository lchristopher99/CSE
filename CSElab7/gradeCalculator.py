# Name: Logan Christopher Date Assigned: 10/24/18
#
# Course: CSE 1284 Sec 11 Date Due: 10/24/18
#
# File name: gradeCalculator.py
#
# Program Description: Program reads grades from a file and returns each individual grade along with an average.

import time
import sys

def main():

  # Loading animation function
  def loading():
    width = 10

    # setup loading bar
    sys.stdout.write("[%s]" % (" " * width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (width+1)) # return to start of line, after '['

    for i in range(width):
      time.sleep(0.1) 
      # update the bar
      sys.stdout.write("-")
      sys.stdout.flush()

    sys.stdout.write("\n")

  # designated function for getting letter grade 
  def getLetterGrade(line):
    ln = int(line)
    if 90 <= ln <= 100:
      l = 'A'
      return l
    elif 80 <= ln < 90:
      l = 'B'
      return l
    elif 70 <= ln < 80: 
      l = 'C'
      return l
    elif 60 <= ln < 70: 
      l = 'D'
      return l
    elif ln < 60: 
      l = 'F'
      return l

  # Prints all grades within file along with average
  def printGrades(fileName):
    # Loading animation
    print('Reading')
    loading()
    print()

    # loop through file and print individual lines along with coresponding grade number
    average = 0
    n = 1
    for line in open(fileName, 'r'):

      l = getLetterGrade(line)
      
      # Prints grade along with letter grade
      print('Grade ' + str(n) + ': ' + l + ' - ' + line, end='')

      average += int(line)
      n += 1

    n -= 1
    average /= n

    print()
    print()
    g = getLetterGrade(average)
    # Prints overall average grade with letter grade
    print('Average Grade: ' + str(g) + ' - ' + str(average))
 
  # Receives file name from user and tests whether it exists or not
  def getFile():
    while True:
      # attempt to get filename from user and if that file exists, move on to printGrades()
      try:
        fileName = input('Please enter file name: ')
        fileExists = open(fileName)
        if fileExists:
          printGrades(fileName)
        break
      # If file not found, throw error
      except FileNotFoundError:
        print('File does not exist. Try again.')
      # If any other error is thrown, exit program
      else:
        break

  getFile()

main()