l = [i for i in range(1,21)]
for _ in range(10):
  a, b = map(int, input().split())
  a-=1
  b-=1
  sub = l[a:b+1].copy()
  sub.reverse()
  l[a:b+1] = sub

print(l)