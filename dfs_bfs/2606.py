def dfs(v):
  visited[v]=1
  network_nodes.append(v)
  for i in graph[v]:
    if visited[i]==0:
      dfs(i)

n = int(input())
m = int(input())
network_nodes = []
cnt=0

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
print(len(network_nodes)-1)
