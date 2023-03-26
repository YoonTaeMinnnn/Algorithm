l = input()
l = list(l)
cnt = 0
stack = [l[0]]

for i in range(1, len(l)):
  if l[i] == ")":
    if l[i-1] == ")":
      stack.pop()
      cnt += 1
    else:
      stack.pop()
      cnt += len(stack)
  else:
    stack.append(l[i])
  print(stack)
print(cnt)
      
      
  