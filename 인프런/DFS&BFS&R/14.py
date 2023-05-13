def DFS(L, b):
  global com
  if L == m:
    result = 0
    for h in house:
      r = 2470000000
      for p in pizza:
        dis = abs(h[0] - p[0]) + abs(h[1] - p[1])
        if dis < r:
          r = dis
      result += r
    if result < com:
      com = result
  else:
    for i in range(len(pizza)):
      if i > b:
        res[L] = pizza[i]
        DFS(L+1, i)
      


n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
res = [0] * m
com = 247000000
pizza = []
house = []
for i in range(n):
  for j in range(n):
    if l[i][j] == 2:
      pizza.append((i,j))
    if l[i][j] == 1:
      house.append((i,j))
DFS(0,-1)
print(com)   