import sys
sys.setrecursionlimit(1000000) #재귀 깊이 늘려주기

def DFS(x,y,h):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<n and 0<=ny<n and l[nx][ny] > h and ch[nx][ny] == 0:
      ch[nx][ny] = 1
      DFS(nx,ny,h)


n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

res_max = -247000000
res_min = 247000000
for i in range(n):
  for j in range(n):
    if l[i][j] > res_max:
      res_max = l[i][j]
    if l[i][j] < res_min:
      res_min = l[i][j]

result = []
for h in range(res_min-1,res_max):
  cnt = 0
  ch = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if l[i][j] > h and ch[i][j] == 0:
        ch[i][j] = 1
        DFS(i,j,h)
        cnt += 1
  result.append(cnt)      

print(max(result))