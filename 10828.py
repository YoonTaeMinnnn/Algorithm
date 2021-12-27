n = int(input())
exec_list = []
for _ in range(n):
  exec_list.append(list(input().split()))

stack = []

for i in exec_list:
  if i[0] == 'push':
    stack.append(int(i[1]))
  if i[0] == 'pop':
    if len(stack)==0:
      print(-1)
    else: 
      print(int(stack.pop()))
  if i[0] == 'size':
    print(len(stack))
  if i[0]=='empty':
    if len(stack)>=1:
      print(0)
    else:
      print(1)
  if i[0] == 'top':
    if len(stack)==0:
      print(-1)
    else:
      print(int(stack[len(stack)-1]))
  
