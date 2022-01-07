import sys
sys.setrecursionlimit(100000)


def dfs(x,y,rang):
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return 
  if graph[x][y]>rang and not visited[x][y]:
    visited[x][y]=True
    dfs(x+1,y,rang)
    dfs(x-1,y,rang)
    dfs(x,y+1,rang)
    dfs(x,y-1,rang)
    return True
  return False

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# start = min(map(min,graph))
end = max(map(max,graph))

compare_list=[]


for r in range(end):
  count=0
  visited = [[False]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if dfs(i,j,r) == True:
        count+=1
  compare_list.append(count)
print(max(compare_list))      
      
