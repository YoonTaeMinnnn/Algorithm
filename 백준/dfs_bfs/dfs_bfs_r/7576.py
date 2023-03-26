from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx>=n or nx<=-1 or ny>=m or ny<=-1:
        continue
      if graph[nx][ny]==0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx,ny))


m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
queue = deque()
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      queue.append((i,j))
bfs()
for i in range(n):
  for j in range(m):
    if graph[i][j]==0:
      print(-1)
      exit(0)
else:
  print(max(map(max,graph))-1)

      

