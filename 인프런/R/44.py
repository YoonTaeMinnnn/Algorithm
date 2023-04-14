from collections import deque

n = int(input())
l=[]
for _ in range(n):
  l.append(list(map(int, input().split())))
t = n // 2
cnt = 0
queue = deque()
queue.append((t,t))

ch = [[0]*n for _ in range(n)]
ch[t][t] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
sum = l[t][t]

while cnt < t:
  size = len(queue)
  for _ in range(size):
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]

      if 0<=nx<n and 0<=ny<n and ch[nx][ny] == 0:
        ch[nx][ny] = 1
        print(l[nx][ny])
        sum += l[nx][ny]
        queue.append((nx,ny))
  cnt += 1
  
print(sum)

  