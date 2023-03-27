from collections import deque

seq = list(input())
n = int(input())
for num in range(1,n+1):
  queue = deque(seq)
  l = list(input())
  for i in l:
    if i in queue:
      if queue.popleft() != i:
        print("#", num, " NO", sep = '')
        break
  else:
    if len(queue) == 0:
      print("#", num, " YES", sep = '')
    else:
      print("#", num, " NO", sep = '')
  


