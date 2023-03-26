import sys
sys.setrecursionlimit(100000)

def dfs(x,y):
  global cnt
  if x<=-1 or x>=m or y>=n or y<=-1:
    return
  if graph[x][y]==0:
    graph[x][y]=1
    cnt+=1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

m,n,k = map(int, sys.stdin.readline().split())
graph = [[0]*n for _ in range(m)]
for _ in range(k):
  x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
  for i in range(m-y2,m-y1):
    for j in range(x1,x2):
      graph[i][j]=1
count = 0
width = []

for i in range(m):
  for j in range(n):
    cnt=0
    if dfs(i,j)==True:    
      count+=1
      width.append(cnt)

width.sort()
print(count)
for i in width:
  print(i, end=' ')