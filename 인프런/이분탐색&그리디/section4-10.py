n = int(input())
l = list(map(int, input().split()))  #[5,3,4,0,2,1,1,0]
sub = [i for i in range(1,n+1)] #[1,2,3,4,5,6,7,8]
result = [n] * n        #[8,8,8,8,8,8,8,8]
for i in range(n):
  cnt = 0
  for j in range(n):
    if cnt == l[i]:
      if result[j] == n:
        result[j] = sub[i]
        break
      else:
        continue
    if result[j] == n:
      cnt += 1

for i in result:
  print(i, end=' ')

