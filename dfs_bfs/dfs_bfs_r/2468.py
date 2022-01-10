import sys
sys.setrecursionlimit(100000)

def dfs(x,y,r):
  if x>=n or x<=-1 or y>=n or y<=-1:
    return
  if graph[x][y]>r and not visited[x][y]:
    visited[x][y]=True
    dfs(x+1,y,r)
    dfs(x-1,y,r)
    dfs(x,y+1,r)
    dfs(x,y-1,r)
    return True
  return False

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_safe = []
graph_max = max(map(max,graph))

for r in range(graph_max):
  count=0
  visited = [[False]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if dfs(i,j,r)==True:
        count+=1
  max_safe.append(count)

print(max(max_safe))
        
