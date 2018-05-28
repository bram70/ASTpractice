import sys

def reverse(str):
  string = ""
  length = len(str)-1
  for x in range(length, -1, -1):
    string = string + str[x]
  return string

stringArray = sys.argv

if len(stringArray)>1:
  test = stringArray[1]
  print reverse(test)
else:
  print "Not enough arguments"
