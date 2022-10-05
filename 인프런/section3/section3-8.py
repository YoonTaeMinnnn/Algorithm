n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
  h, direct, c = map(int, input().split())
  # h : 행, direct : 방향( 0:왼쪽, 1:오른쪽 ), c : 횟수
  sub = l[h-1].copy()
  for i in range(n):
    if direct == 1:
      l[h-1][(i+c)%n] = sub[i]
    else:
      l[h-1][(i-c)%n] = sub[i]

s = 0
e = n
k = n // 2
sum = 0
for i in range(n):
  for j in range(s, e):
    sum += l[i][j]
  if i < k:
    s += 1
    e -= 1
  else:
    s -= 1
    e += 1

print(sum)


