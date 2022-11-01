from collections import deque

n, m = map(int, input().split())
l = list(map(int, input().split()))
q = [(pos, val) for pos, val in enumerate(l)]
queue = deque(q)
cnt = 0
while True:
  a = queue.popleft()
  for i in queue:
    if a[1] < i[1]:
      queue.append(a)
      break
  else:
    cnt += 1
    if a[0] == m:
      print(cnt)
      break
    
    


