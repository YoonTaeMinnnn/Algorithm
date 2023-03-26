l = input()
l = list(l)
stack = []
result = 0

for i in l:
  if i.isdecimal():
    stack.append(i)
  else:
    result = eval(stack[-2] + i + stack[-1])
    stack.pop()
    stack.pop()
    stack.append(str(result))

print(result)

