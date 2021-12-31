def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if metrics[x,y]==0:
    metrics[x,y]==1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False


n, m = map(int,input().split())
metrics = []
for _ in range(n):
  metrics.append(list(map(int,input())))
print(metrics)

cnt=0
for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      cnt+=1

print(cnt)