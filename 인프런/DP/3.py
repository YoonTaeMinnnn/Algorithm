n = int(input())
l = list(map(int, input().split()))
l.insert(0,0)
dy = [0] * (n+1)
dy[1] = 1
res = 0

for i in range(2,n+1):
  max = 0
  for j in range(i-1,0,-1):
    if l[i] > l[j] and max < dy[j]:
      max = dy[j]
  dy[i] = max + 1
  if dy[i] > res:
    res = dy[i]
    
print(res)