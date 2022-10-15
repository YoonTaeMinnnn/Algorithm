n = int(input())
l = []
for _ in range(n):
  l.append(list(map(int, input().split())))
l = sorted(l, key=lambda x:(x[1], x[1]-x[0]))

a = l[0][1]
cnt = 1
for i in range(1,n):
  if a <= l[i][0]:
    a = l[i][1]
    cnt += 1

print(cnt)

