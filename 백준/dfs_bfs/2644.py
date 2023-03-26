count = 0 

def dfs(v,v2):
  global count
  count+=1
  print('v : ',v)
  print('v2 : ',v2)
  print('----------------------')
  if v == v2:
    return count
  visited[v]=True
  for i in graph[v]:
    if not visited[i]:
      dfs(i,v2)
        
        


n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

print(graph)
dfs(a,b)
print(count)

