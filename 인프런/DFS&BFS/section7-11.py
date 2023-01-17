def DFS(x, y):
  global cnt
  if x == end_x and y == end_y:
    cnt+=1
  else:
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y

      if 0<=nx<n and 0<=ny<n and l[x][y] < l[nx][ny] and ch[nx][ny] == 0:
        ch[nx][ny] = 1
        DFS(nx,ny)
        ch[nx][ny] = 0
        

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
ch = [[0]*n for _ in range(n)]
ch[0][0] = 1
cnt = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max = -2147000000
min = 2147000000

for i in range(n):
  for j in range(n):
    if l[i][j] < min:
      min = l[i][j]
      start_x = i
      start_y = j
    if l[i][j] > max:
      max = l[i][j]
      end_x = i
      end_y = j

DFS(start_x, start_y)
print(cnt)
  
