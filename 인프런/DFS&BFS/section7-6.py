def DFS(L, P):
  if L == n:
    for j in range(P):
      print(res[j], end=" ")
    print()
  else:
    for i in range(1,27):
      if code[L] == i:
        res[P] = i
        DFS(L+1, P+1)
      elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
        res[P] = i
        DFS(L+2, P+1)

code = list(map(int, input()))
n = len(code)
code.append(-1) #out of range 방지
res = [0] * (n+3)
DFS(0,0)
