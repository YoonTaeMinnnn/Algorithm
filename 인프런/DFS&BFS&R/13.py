import sys
# sys.setrecursionlimit(10000000)

def DFS(x,y):
  if x == 0:
    print(y)
    sys.exit(0)
  else:
    for i in range(3):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<10 and 0<=ny<10 and l[nx][ny] == 1:
        l[nx][ny] = 0
        DFS(nx,ny)
        
dx = [0,0,-1]
dy = [1,-1,0]
l = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
  if l[9][i] == 2:
    DFS(9,i)