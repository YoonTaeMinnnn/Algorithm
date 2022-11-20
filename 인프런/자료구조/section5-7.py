from collections import deque
turn = list(input())
n = int(input())
result = []

for _ in range(n):
  queue = deque(turn)
  a = queue.popleft()
  l = list(input())
  for i in l:
    if i in turn:
      if a != i:
        queue = deque([])
        result.append("NO")
        break
    if a == i:
      if len(queue) == 0:
        result.append("YES")
        break
      a = queue.popleft()
  else:
    if len(queue) >= 0:
      result.append("NO")
  

for i, v in enumerate(result):
  print("#%d"%(i+1), "%s"%v)


#CBDAGE FGCDAB CTSBDEA

# AFC
# 1
# AFFDCCFF