# Name: Logan Christopher Date Assigned: 11/14/18
#
# Course: CSE 1284 Sec 11 Date Due: 11/14/18
#
# File name: reading_level.py
#
# Program Description: Program calculates reading level of a given text.

import urllib
from urllib.request import urlopen

def calc_level(ASL, ASW):
  level = (0.39 * ASL) + (11.8 * ASW) - 15.59
  return level

def get_ASL(word_list):
  sent_count = len(word_list)
  word_count = 0
  for sent in word_list:
    word_count += len(sent)

  ASL = word_count / sent_count

  return ASL, word_count

def get_ASW(word_list, word_count):
  syl_count = 0
  for sent in word_list:
    for word in sent:
      if len(word) % 4:
        syl_count += len(word) % 4
  
  ASW = syl_count / word_count

  return ASW

def get_wordList(text):
  sent_list = text.split('.')
  i = 0
  word_list = []
  for line in sent_list:
    word_list.append(sent_list[i].split(' '))
    i += 1

  return word_list

def main():
  url = 'http://www.gutenberg.org/cache/epub/18857/pg18857.txt'
  page = urllib.request.urlopen(url)
  text = page.read().decode('utf8')

  word_list = get_wordList(text)
  ASL, word_count = get_ASL(word_list)
  ASW = get_ASW(word_list, word_count)
  level = calc_level(ASL, ASW)

  print('Average syllables per word:', ASW)
  print('Average sentence length:', ASL)
  print('Reading level:', level)

main()