from collections import deque
import sys

m, n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
  for j in range(m):
    if l[i][j] == 1:
      queue.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<m and l[nx][ny] == 0:
      l[nx][ny] = l[x][y] + 1
      queue.append((nx,ny))

res = -247000000

for i in range(n):
  for j in range(m):
    if l[i][j] == 0:
      print(-1)
      sys.exit(0)
    if l[i][j] > res:
      res = l[i][j]
if res == 1:
  print(0)
else:
  print(res-1)
      
