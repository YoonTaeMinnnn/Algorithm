import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  l = []
  for _ in range(n):
    l.append(list(map(int, input().split())))
  l.sort(key = lambda x : x[0])
  top = 0
  cnt = 1
  for i in range(1,n):
    if l[i][1] < l[top][1]:
      top = i
      cnt += 1
  print(cnt)

