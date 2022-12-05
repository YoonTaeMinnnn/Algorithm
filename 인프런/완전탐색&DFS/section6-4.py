import sys

def DFS(v):
  global signal
  if v == n:
    asum = 0
    bsum = 0
    for i in range(n):
      if ch[l[i]] == 1:
        asum += l[i]
      else:
        bsum += l[i]
    if asum == bsum:
      print("YES")
      sys.exit(0)
  else:
    ch[l[v]] = 1
    DFS(v+1)
    ch[l[v]] = 0
    DFS(v+1)

n = int(input())
l = list(map(int, input().split()))
ch = [0] * (max(l) + 1)
DFS(0)
print("NO")