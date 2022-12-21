def DFS(ch, V, visited):
  global cnt
  visited[V] = True
  for i in ch[V]:
    if not visited[V]:
      DFS(V)
  cnt += 1

cnt = 0
n, m = map(int, input().split())
ch = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
  a, b = map(int, input().split())
  ch[a].append(b)
print(ch)
print(visited)
DFS(ch, 1, visited)
print(cnt)


# 5 9 
# 1 2  
# 1 3 
# 1 4 
# 2 1 
# 2 3 
# 2 5 
# 3 4 
# 4 2 
# 4 5