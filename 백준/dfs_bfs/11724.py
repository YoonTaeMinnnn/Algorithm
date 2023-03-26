import sys

sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
  visited[v]=1
  for i in graph[v]:
    if visited[i]==0:
      dfs(graph,i,visited)
    
n, m =map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,n+1):
  graph[i].sort()

visited=[0]*(n+1)

count=0
for i in range(1,n+1):
  if visited[i]==0:
    count+=1
    dfs(graph,i,visited)
print(count)

# import sys

# sys.setrecursionlimit(10000)

# N, M = map(int, sys.stdin.readline().split())

# graph = [[] for _ in range(N+1)]
# graph[0] = [0,0]
# visited = [False for _ in range(N+1)]

# count = 0

# for _ in range(M):
#     start, end = map(int, sys.stdin.readline().split())
#     graph[start].append(end)
#     graph[end].append(start)
#     graph[start].sort()
#     graph[end].sort()


# def DFS(graph, start, visited):
#     visited[start] = True

#     for i in graph[start]:
#         if not visited[i]:
#             DFS(graph, i, visited)


# for i in range(1, len(visited)):
#     if visited[i] == False:
#         count += 1
#         DFS(graph, i, visited)

# print(count)