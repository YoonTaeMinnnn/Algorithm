from collections import deque

def bfs(v):
  queue = deque()
  queue.append(v)
  while queue:
    v = queue.popleft()
    if v==k:
      return graph[v]
    for i in (v+1,v-1,v*2):
      x = i
      if 0<=x<=MAX and not graph[x]:
        queue.append(x)
        graph[x] = graph[v] + 1
        
  
  
n, k = map(int, input().split())
MAX = 10**5
graph = [0]*(MAX+1)

print(bfs(n))

  

