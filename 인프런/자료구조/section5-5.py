from collections import deque

n, k = map(int, input().split())
n = [i for i in range(1,n+1)]
cnt = 1
queue = deque(n)
while len(queue) > 1:
  if cnt == k:
    queue.popleft()
    cnt = 1
    continue
  else:
    a = queue.popleft()
    queue.append(a)
    cnt += 1
    
print(queue.popleft())
  
  