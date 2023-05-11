def DFS(x,y):
  global cnt
  cnt += 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and l[nx][ny] == 1:
      l[nx][ny] = 0
      DFS(nx,ny)


n = int(input())
l = [list(map(int, input())) for _ in range(n)]
cnt = 0
num = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
  for j in range(n):
    if l[i][j] == 1:
      l[i][j] = 0
      cnt = 0
      DFS(i,j)
      num.append(cnt)
      
num.sort()
print(len(num))
for i in num:
  print(i)