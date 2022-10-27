l = list(input())
stack = []
for i in l:
  if i.isdigit():
    stack.append(i)
  else:
    a = stack.pop()
    b = stack.pop()
    result = eval(b+i+a)
    stack.append(str(result))

print(result)
