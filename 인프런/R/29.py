import sys

def DFS(v, s):
  if s > total // 2:
    return
  if v == n:
    if s == total - s:
      print("YES")
      sys.exit(0)
  else:
    DFS(v+1, s + l[v])
    DFS(v+1, s)
  
n = int(input())
l = list(map(int, input().split()))
total = sum(l) 

DFS(0,0)
print("NO")