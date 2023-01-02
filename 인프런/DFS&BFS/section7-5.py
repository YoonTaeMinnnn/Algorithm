def DFS(L):
  global result
  if L == n:
    s = max(res) - min(res)
    if s < result:
      if len(set(res)) == 3:
        result = s
  else:
    for i in range(3):
      res[i] += l[L]
      DFS(L+1)
      res[i] -= l[L]

    
n = int(input())
l = [int(input()) for _ in range(n)]
res = [0] * 3
result = 100000000
DFS(0)
print(result)