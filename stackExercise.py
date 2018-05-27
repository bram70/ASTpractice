from Models.stack import Stack
import sys
import re

# Given an string of a math expresion
# write a program to test if the number of [ and {
# are the same as }]

# My algorithm is to store the number of { [ (
# and accumulate with a counter
# substract the number when the same closing symbols
# follows the expression

# test 1: [](){} should return True
# test 2: [({)}] should return False
# test 3: [{()}] should return True
# test 4 ([{}]) should return True


def retrieveCloseCharacter(char):
  if char == '(':
    return ')'
  if char == '{':
    return '}'
  if char == '[':
    return ']'

def isOpener(char):
  if char == '(' or char == '{' or char == '[':
    return True
  return False

def isCloser(char):
  if char == ')' or char == '}' or char == ']':
    return True
  return False

argument = sys.argv
if len(argument) > 1:
  testingString = argument[1]
  token_list = re.split("([^0-9])", testingString)
  print token_list
  currentOpener = ''
  stack = Stack()
  for character in token_list:
    if character == '' or character == ' ':
      continue
    if isOpener(character):
      stack.push(character)
      continue
    if isCloser(character):
      currentOpener = stack.pop()
      if not retrieveCloseCharacter(currentOpener)==character:
        print False 
        sys.exit()
  print True
else:
  print "no arguments"
