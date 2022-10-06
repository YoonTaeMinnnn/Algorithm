n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
l.insert(0, [0] * (n+2))
l.append([0] * (n+2))

for i in range(1, n+1):
  l[i].insert(0, 0)
  l[i].append(0)
  
cnt = 0

for i in range(1,n+1):
  for j in range(1, n+1):
    right = l[i][j+1]
    left = l[i][j-1]
    up = l[i-1][j]
    down = l[i+1][j]
    if l[i][j] > right and l[i][j] > left and l[i][j] > up and l[i][j] > down:
      cnt += 1

print(cnt)

# ---------------강사 풀이-------------------

dx = [1,-1, 0, 0]
dy = [0 ,0, 1, -1]
for i in range(1, n+1):
  for j in range(1, n+1):
    if all(l[i][j] > l[i + dx[k]][j + dy[k]] for k in range(4)):
      cnt += 1 

print(cnt)
    