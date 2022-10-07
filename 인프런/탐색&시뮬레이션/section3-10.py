import sys

l = [list(map(int, input().split())) for _ in range(9)]
z = 0
for i in range(9):
  n = [0] * 10
  m = [0] * 10
  for j in range(9):
    a = l[i][j]
    b = l[j][i]
    if n[a] == 1 or m[b] == 1:
      print('NO')
      sys.exit()
    n[a] = 1
    m[b] = 1


for i in range(0,9,3):
  for j in range(0,9,3):
    a = l[:i+3][:j+3]
    for z in range(3):
      k = [0] * 10
      for w in range(3):
        b = a[z][w]
        if k[b] == 1:
          print('NO')
          sys.exit()
        k[b] = 1
   
print('YES')
    
