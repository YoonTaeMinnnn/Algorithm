def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return
  if graph[x][y]=='R':
    graph[x][y]='RR'
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    return True
  return False

n = int(input())
graph = [list(input()) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if graph[i][j]=='G':
      graph[i][j]='R'

count=0
cnt = 0
for i in range(n):
  for j in range(n):
    if dfs(i,j)=='R':
      count+=1
    elif dfs(i,j)=='B':
      cnt+=1

print(count)
print(cnt)
