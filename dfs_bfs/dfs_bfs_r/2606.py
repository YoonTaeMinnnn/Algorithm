def dfs(graph,v,visited):
  global count
  visited[v]=True
  count+=1
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)


n = int(input())
k = int(input())
count=0

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(k):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(graph,1,visited)
print(count-1)


