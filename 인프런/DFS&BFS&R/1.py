def DFS(L, s, t):
  global res
  if t > total:
    return 
  if L == n:
    if s > res:
      res = s
  else:
    DFS(L+1, s+l[L][0], t+l[L][1])
    DFS(L+1, s, t)

n, total = map(int, input().split())
l = []
res = 0
for _ in range(n):
  score, time = map(int ,input().split())
  l.append((score, time))
DFS(0,0,0)
print(res)
