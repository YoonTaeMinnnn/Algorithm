def DFS(L, P):
  global cnt
  if L == size:
    cnt += 1
    for i in range(P):
      print(chr(res[i]+64), end='')
    print()
  else:
    for i in range(1,27):
      if l[L] == i:
        res[P] = i
        DFS(L+1, P+1)
      elif i >= 10 and l[L] == i//10 and l[L+1] == i%10:
        res[P] = i
        DFS(L+2, P+1)
  
  
l = list(map(int, input()))
size = len(l)
l.append(-1)
res = [0] * size
cnt = 0
DFS(0,0)
print(cnt)



