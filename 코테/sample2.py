a = [2,1,2]
a = [[i,0] for i in a]
s = len(a)
for i in range(s):
  if i == s-1:
    if (a[0][0] + a[i][0]) % 2 == 0:
      a[0][1] = 1
      a[i][1] = 1
  elif (a[i][0] + a[i+1][0]) % 2 == 0:
    a[i][1] = 1
    a[i+1][1] = 1

cnt = 0
for i in a:
  if i[1] == 1:
    cnt += 1

print(cnt//2)
  
