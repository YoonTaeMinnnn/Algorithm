def dfs(x,y):
  if x<=-1 or x>=m or y<=-1 or y>=n:
    return 
  if graph[x][y]==1:
    graph[x][y]==0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

test = int(input())

for i in range(test):
  cnt = 0
  n, m, k = map(int,input().split())
  graph = [[0]*m for _ in range(n)]
  result = 0
  for j in range(k):
    x, y = map(int, input().split())
    graph[x][y] = 1

  for i in range(n):
    for j in range(m):
      if dfs(i,j)==True:
        result+=1
  print(result)
      

