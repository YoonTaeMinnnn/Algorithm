n = int(input())
l = []
for _ in range(n):
  start, end = map(int, input().split())
  l.append((start, end))
l.sort(key = lambda x : (x[1], x[0]))
cnt = 0
com = l[0][1]
for i in range(1,len(l)):
  if com <= l[i][0]:
    cnt += 1
    com = l[i][1]
    
print(cnt+1)