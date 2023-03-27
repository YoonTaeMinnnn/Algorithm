from collections import deque

n, k = map(int, input().split())
l = [i for i in range(1,n+1)]
queue = deque(l)
cnt = 1
while len(queue) > 1:
  if cnt == k:
    cnt = 1
    queue.popleft()
    continue
  queue.append(queue.popleft())
  cnt += 1

print(queue.popleft())