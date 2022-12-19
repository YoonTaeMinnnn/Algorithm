def DFS(L, s, b):
  global cnt
  if L == k:
    if s % m == 0:
      cnt += 1
  else:
    for i in l:
      if i > b:
        DFS(L+1, s+i, i)
    

cnt = 0
n, k = map(int, input().split())
l = list(map(int, input().split()))
m = int(input())
DFS(0, 0, 0)
print(cnt)