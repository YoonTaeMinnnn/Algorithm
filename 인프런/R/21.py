from collections import deque
n, m = map(int, input().split())
l = list(map(int, input().split()))
l = [(i, v) for i, v in enumerate(l)]
cnt = 0
queue = deque(l)

while True:
  a = queue.popleft()
  if any(a[1] < i[1] for i in queue):
    queue.append(a)
  else:
    print(a)
    cnt += 1
    if a[0] == m:
      print(cnt)
      break


    
      
  