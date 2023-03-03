# 메모이제이션 방식
def DFS(len):
  if len == 1 or len == 2:
    return len
  dy[len] = DFS(len-1) + DFS(len-2)
  return dy[len]

n = int(input())
dy = [0] * (n+1)
print(DFS(n))