
def DFS(s, c):
  global res
  if s > m:
    return
  if s == m:
    if res > c:
      res = c
  else:
    for i in range(n):
      DFS(s+l[i], c + 1)

# 5 2 1
n = int(input())
l = list(map(int, input().split()))
l.sort(reverse= True)
m = int(input())
res = 147000000
DFS(0, 0)
print(res)