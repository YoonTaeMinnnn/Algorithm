def DFS(L, s, t):
  global res
  if t > m:
    return
  if L == n:
    if s > res:
      res = s
  else:
    DFS(L+1, s+l[L][0], t+l[L][1])
    DFS(L+1, s, t)

res = 0
n, m = map(int, input().split())
l = []
for _ in range(n):
  a, b = map(int, input().split())
  l.append((a,b))
  
DFS(0,0,0)
print(res)
