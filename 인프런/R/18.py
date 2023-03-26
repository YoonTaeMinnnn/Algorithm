l = input()
l = list(l)
stack = []
result = ""

for i in l:
  if i=="*" or i=="/":
    while stack and (stack[-1] == "*" or stack[-1] == "/"):
      result += stack.pop()
    stack.append(i)
  elif i =="+" or i == "-":
    while stack and stack[-1] != "(":
      result += stack.pop()
    stack.append(i)
  elif i == "(":
    stack.append(i)
  elif i == ")":
    while stack and stack[-1] != "(":
      result += stack.pop()
    stack.pop()
  else:
    result += i

while stack:
  result += stack.pop()
print(result)
    
  