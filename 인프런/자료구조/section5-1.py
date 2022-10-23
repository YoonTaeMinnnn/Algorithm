a, m = map(int, input().split())
a = str(a)
l = []
for i in a:
    l.append(int(i))
stack = []
for i in l:
  while stack and m>0 and stack[-1] < i:
    stack.pop()
    m -= 1
  stack.append(i)

if m > 0:
  stack = stack[:-m]
  
print(*stack)
  