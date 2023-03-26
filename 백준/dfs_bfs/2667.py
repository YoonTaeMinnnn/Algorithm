def dfs(x,y):
  global count
  if x<=-1 or x>=n or y<=-1 or y>=n:
    return
  if graph[x][y] == 1:
    graph[x][y]=0
    count+=1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

n = int(input())
graph=[]
for _ in range(n):
  graph.append(list(map(int, input())))

result=0
apart_count=[]

for i in range(n):
  for j in range(n):
    count=0
    if dfs(i,j)==True:
      result+=1
      apart_count.append(count)

apart_count.sort()
print(result)
for i in apart_count:
  print(i)



