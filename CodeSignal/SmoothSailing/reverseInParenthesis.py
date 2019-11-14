def reverseInParentheses(inputString):
  start,end = 0,0
  started = False
  count = 0
  new_string = ""
  for i in range(len(inputString)):
    if inputString[i] == "(" and started == False:
      started = True
      start = i
    if inputString[i] == "(" and started == True:
      count += 1
    if inputString[i] == ")":
      count -= 1
    if count == 0 and started == True:
      end = i
      break

  print (f'input {inputString}, start {start}, end {end}')

  if started == True:
    new_string = inputString[0:start] + reverseInParentheses( reverse(inputString[start+1:end]) + inputString[end+1:])
  else:
    new_string = inputString
  return new_string



def reverse(s):
  str = ""
  for i in s:
    j = i
    if i == "(":
      j = ")"
    if i == ")":
      j = "("
    str = j + str
  return str
