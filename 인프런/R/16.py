n, m = input().split()

l = list(n)
l = list(map(int, l))
m = int(m)
stack = []
for i in l:
  while stack and m>0 and stack[-1]<i:
    stack.pop()
    m -= 1
  stack.append(i)

if m > 0:
  stack = stack[:-m]

for i in stack:
  print(i, sep='', end='')
  