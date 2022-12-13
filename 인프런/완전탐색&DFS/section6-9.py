import sys

def DFS(L, s):
  if L == n and s == m:
    print(*p)
    sys.exit(0)
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1
        p[L] = i
        DFS(L+1, s+(p[L]*b[L]))
        ch[i] = 0

n, m = map(int, input().split())
ch = [0] * (n+1)
b = [1] * n
for i in range(1, n):
  b[i] = b[i-1] * (n-i) // i
p = [0] * n
DFS(0,0)
  
  




  
