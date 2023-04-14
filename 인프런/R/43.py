from collections import deque

s, e = map(int, input().split())
max = 10000
dis = [0] * (max+1)
ch = [0] * (max+1)
queue = deque([s])

while queue:
  a = queue.popleft()
  if a == e:
    break
  for i in (a+1, a-1, a+5):
    if ch[i] == 0:
      ch[i] = 1
      dis[i] = dis[a] + 1
      queue.append(i)

print(dis[e])