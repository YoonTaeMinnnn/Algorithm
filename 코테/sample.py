
# 1 1 0 1
s = ""
cnt = 0
def DFS(n):
  global cnt
  if n == 0:
    return 
  if n % 2 == 1:
    cnt += 1
  DFS(n // 2)

DFS(13)
print(cnt)