def DFS(L, sum):
  global res
  if L == k:
    res.add(abs(sum))
  else:
    DFS(L+1, sum + l[L])
    DFS(L+1, sum - l[L])
    DFS(L+1, sum)

k = int(input())
l = list(map(int, input().split()))
s = sum(l)
res = set()
DFS(0,0)
print(s - len(res) + 1)