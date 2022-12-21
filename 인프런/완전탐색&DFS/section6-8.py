def DFS(L):
  global ch
  global cnt
  if L == m:
    print(*res)
    cnt += 1
  else:
    for i in range(1, n+1):
      if ch[i] == 0:
        ch[i] = 1
        res[L] = i
        DFS(L+1)
        ch[i] = 0


n, m = map(int, input().split())
ch = [0] * (n+1)
res = [0] * m
cnt = 0
DFS(0)
print(cnt)


# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# ....