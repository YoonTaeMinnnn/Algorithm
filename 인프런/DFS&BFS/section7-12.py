def DFS(x, y):
  global cmt
  cmt += 1
  l[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and l[nx][ny] == 1:
      DFS(nx, ny)
      
  return True

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n = int(input())
l = [list(map(int, input())) for _ in range(n)]
cmt = 0
result = []

for i in range(n):
  for j in range(n):
    if l[i][j] == 1:
      DFS(i, j)
      result.append(cmt)
      cmt = 0

print(len(result))
result.sort()
for i in result:
  print(i)




