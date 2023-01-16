def DFS(x, y):
  global cnt
  if x == 6 and y == 6:
    cnt+=1
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<=6 and 0<=ny<=6 and l[nx][ny] == 0:
        l[nx][ny] = 1
        DFS(nx,ny)
        l[nx][ny] = 0
        
    

dx = [1,-1,0,0]
dy = [0,0,1,-1]
l = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
l[0][0] = 1
DFS(0,0)
print(cnt)

