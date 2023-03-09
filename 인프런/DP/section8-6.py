n = int(input())
l = []
for _ in range(n):
  l.append(tuple(map(int, input().split())))
l.sort(key = lambda x : x[0], reverse = True)
dy = [0] * n
dy[0] = l[0][1]
res = 0

for i in range(1,n):
  max = 0
  for j in range(i-1, -1, -1):
    if l[i][2] < l[j][2] and dy[j] > max:
      max = dy[j]
  dy[i] = max + l[i][1]
  if dy[i] > res:
    res = dy[i]

print(res)