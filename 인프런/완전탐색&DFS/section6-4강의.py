import sys

def DFS(v, s):
  if s > total // 2:
    return 
  if v == n:
    if s == total - s:
      print("YES")
      sys.exit(0)      
  else:
    DFS(v+1, s+l[v]) #부분집합 포함한 경우
    DFS(v+1, s) #부분집합 포함하지 않은 경우


n = int(input())
l = list(map(int, input().split()))
total = sum(l)
DFS(0,0)
print("NO")