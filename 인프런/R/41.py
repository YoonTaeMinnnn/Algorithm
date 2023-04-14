def DFS(L):
  global res
  if L == n:
    c = max(money) - min(money)
    if c < res:
      if len(set(money)) == 3:
        res = c
  else:
    for i in range(3):
      money[i] += l[L]
      DFS(L+1)
      money[i] -= l[L]

n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
money = [0] * 3
res = 147000000
DFS(0)
print(res)