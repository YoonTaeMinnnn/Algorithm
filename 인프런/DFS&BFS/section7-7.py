from collections import deque

s, e = map(int, input().split())
max = 10000
ch = [0] * (max+1)
dis = [0] * (max+1)
ch[s] = 1
dis[s] = 0
queue = deque()
queue.append(s)

while queue:
  now = queue.popleft()
  if now == e:
    break
  for next in (now+1, now-1, now+5):
    if 0<next<=max:
      if ch[next] == 0:
        ch[next] = 1
        queue.append(next)
        dis[next] = dis[now] + 1

print(dis[e])