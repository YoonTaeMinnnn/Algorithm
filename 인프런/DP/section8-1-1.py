def DFS(len):
  if len == 1:
    return 1
  if len == 2:
    return 2
  return DFS(len-1) + DFS(len-2)

n = int(input())
dy = [0] *(n+1)
print(DFS(n))