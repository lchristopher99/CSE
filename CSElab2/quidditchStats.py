# Name: Logan Christopher Assigned: 9/12/18
#
# Course: CSE 1284 Section: 11 Date Due: 9/12/18
#
# File name: quidditchStats.py
#
# Program Description: Calculates statistics of a Quidditch match based off of user input.

print('The following is a quidditch stats calculator.')
print('Enter the match information below and the according statistcs will be generated.')

print()

teamA = input('Enter the name of the team who caught the golden snitch: ')
scoreA = input('What was the teams final score? ')
teamB = input('Enter the name of the other team: ')
scoreB = input('What was the teams final score? ')
length = input('Enter the length of the game in minutes: ')
print()

length = int(length)
scoreB = int(scoreB)
scoreA = int(scoreA)

if scoreA > 150:
  scoreA = scoreA - 150
  scoreA = scoreA / 10
  gpmA = scoreA / length

  print('First Team Statistics:')
  print('------------------------------')
  print('House: ', teamA)
  print('Goals: ', scoreA)
  print('Snitch: 1')
  print('Goals per Minute: ', gpmA)
  print()

  scoreB = scoreB / 10
  gpmB = scoreB / length

  print('Second Team Statistics:')
  print('------------------------------')
  print('House: ', teamB)
  print('Goals: ', scoreB)
  print('Snitch: 0')
  print('Goals per Minute: ', gpmB)
else:
  print('Final score of the team that caught the snitch must be at least 150, due to the snitch being 150 points by itself.')
  
