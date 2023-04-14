def DFS(L,s):
  global cnt
  if s > t:
    return
  if L == k:
    if s == t:
      cnt += 1
  else:
    for i in range(l[L][1] + 1):
      DFS(L+1, s+(l[L][0] * i))

t = int(input())
k = int(input())
l = []
for _ in range(k):
  p, n = map(int, input().split())
  l.append((p,n))
cnt = 0
DFS(0,0)
print(cnt)
