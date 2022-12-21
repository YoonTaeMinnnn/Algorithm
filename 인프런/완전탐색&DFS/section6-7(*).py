def DFS(L, sum):
  global res
  if sum > m:
    return
  if sum == m:
    if L < res:
      res = L
  else:
    for i in l:
      DFS(L+1, sum+i)
    
n = int(input())
l = list(map(int, input().split()))
m = int(input())
res = 247000000
l.sort(reverse=True)
DFS(0,0)
print(res)


  