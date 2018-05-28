import sys

lineArguments = sys.argv
if len(lineArguments) == 3:
  testString1 = lineArguments[1]
  testString2 = lineArguments[2]
  found = True
  for i in range(len(testString1)):
    found = True
    for j in range(len(testString2)): 
      if i+j >= len(testString1):
        found = False
        break
      if testString2[j] != testString1[i+j]:
        found = False
    if found:
      print True
      found = True
      break
  if not found:
    print False
else:
  print "not enough args"
