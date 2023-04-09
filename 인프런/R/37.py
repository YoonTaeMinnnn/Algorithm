def DFS(L, s, c):
  global cnt
  if L == k:
    if s % m == 0:
      cnt += 1
  else:
    for i in range(c, len(l)):
      DFS(L+1, s+l[i], i+1)

# 2 4 5 8 12

n, k = map(int, input().split())
l = list(map(int, input().split()))
m = int(input())
cnt = 0
DFS(0,0,0)
print(cnt)