def DFS(L, sum):
  global cnt
  if sum > t:
    return
  if L == k:
    if sum == t:
      cnt += 1
  else:
    for i in range(l[L][1]+1): # 0123
      DFS(L+1, sum + l[L][0]*i)
      

t = int(input())
k = int(input())
l = []
cnt = 0
for _ in range(k):
  p, n = map(int, input().split())
  l.append((p,n))
DFS(0,0)
print(cnt)
