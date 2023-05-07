def DFS(L):
  global result
  if L == n:
    if len(set(res)) < 3:
      return
    else:
      r = max(res) - min(res)
      if r < result:
        result = r
  else:
    for i in range(3):
      res[i] += l[L]
      DFS(L+1)
      res[i] -= l[L]


n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
res = [0] * 3
result = 247000000
DFS(0)
print(result)