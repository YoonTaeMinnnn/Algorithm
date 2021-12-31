from collections import deque

def dfs(v):
  print(v, end=' ')
  visited_dfs[v]=1
  for i in graph[v]:
    if visited_dfs[i]==0:
      dfs(i)

def bfs(v):
  queue = deque([v])
  visited_bfs[v]=1
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if visited_bfs[i]==0:
        queue.append(i)
        visited_bfs[i]=1
  


n, m, v = map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a,b = map(int,input().split())  
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,n+1):
  graph[i].sort()

visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

dfs(v)
print()
bfs(v)
  