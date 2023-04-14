def DFS(L, s):
  global res
  if L > n+1:
    return
  if L == n+1:
    if res < s:
      res = s
  else:
    DFS(L + l[L][0], s + l[L][1])
    DFS(L+1, s)

n = int(input())
l = [0]
for _ in range(n):
  t, p = map(int, input().split())
  l.append((t,p))
print(l)
res = 0
DFS(1,0)
print(res)
