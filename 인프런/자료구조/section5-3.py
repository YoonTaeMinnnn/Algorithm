prefix = list(input())
stack = ['^']
result =''
sub = ['*', '/', '+', '-']
for i in prefix:
  if i.isdecimal():
    result += i
  elif i == '(':
    stack.append(i)
  elif i ==')':
    while True:
      if stack[-1] == '(':
        stack.pop()
        break
      result += stack.pop()
  else:
    if i == '*' or i =='/':
      while True:
        a = stack[-1]
        if a =='*' or a =='/':
          result += stack.pop()
        else:
          break
      stack.append(i)
    elif i =='+' or i =='-':
      while True:
        a = stack[-1]
        if a =='*' or a=='/' or a =='+' or a =='-':
          result += stack.pop()
        else:
          break   
      stack.append(i)
  

while stack:
  result += stack.pop()
print(result[:-1])

