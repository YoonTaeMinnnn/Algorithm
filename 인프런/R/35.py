import sys

def DFS(L, s):
  if L == n and s == f:
    print(*p)
    sys.exit(0)
  else:
    for i in range(1, n+1):
      if visited[i] == 0:
        visited[i] = 1
        p[L] = i
        DFS(L+1, s+(p[L]*b[L]))
        visited[i] = 0

n, f = map(int, input().split())
visited = [0] * (n+1)
p = [0] * n
b = [1] * n
for i in range(1, n):
  b[i] = b[i-1] * (n-i) // i
DFS(0,0)