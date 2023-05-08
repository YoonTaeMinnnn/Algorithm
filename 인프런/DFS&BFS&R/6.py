from collections import deque

s, e = map(int, input().split())
max = 10000
dis = [0] * max
vis = [0] * max
vis[s] = 1
queue = deque([s])
while True:
  a = queue.popleft()
  if a == e:
    print(dis[a])
    break
  for i in (a+1, a-1, a+5):
    if 0<i<=max:
      if vis[i] == 0:
        vis[i] = 1
        dis[i] = dis[a] + 1
        queue.append(i)