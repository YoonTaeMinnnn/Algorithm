def DFS(L, time, grade):
  global res
  if time > m:
    return
  if L == n:
    if time <= m:
      if grade > res:
        res = grade
  else:
    DFS(L+1, time + l[L][1], grade + l[L][0])
    DFS(L+1, time, grade)
      
  

n, m = map(int, input().split())
l = []
for _ in range(n):
  a, b = map(int, input().split())
  l.append((a,b))
print(l)
res = 0
DFS(0,0,0)
print(res)
