n, m = map(int, input().split())
l = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
  row, col, cost = map(int, input().split())
  l[row][col] = cost

for i in range(1, n+1):
  for j in range(1, n+1):
    print(l[i][j],end=" ")
  print()