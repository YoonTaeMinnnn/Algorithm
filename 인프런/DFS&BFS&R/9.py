def DFS(x, y):
  global cnt
  if (x,y) == (maxx, maxy):
    cnt += 1
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<n and 0<=ny<n and l[x][y] < l[nx][ny] and vis[nx][ny] == 0:
        vis[nx][ny] = 1
        DFS(nx, ny)
        vis[nx][ny] = 0

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

min = 247000000
max = 0
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
vis = [[0] * n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if l[i][j] < min:
      min = l[i][j]
      minx = i
      miny = j
    if l[i][j] > max:
      max = l[i][j]
      maxx = i
      maxy = j

vis[minx][miny] = 1

DFS(minx,miny)
print(cnt)