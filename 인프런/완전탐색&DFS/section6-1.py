import math

l = [int(math.pow(2,i)) for i in range(10)]
index = []
def result(n):
  if n <= 0:
    return
  for k, v in enumerate(l):
    if n < v:
      index.append(k-1)
      return result(n-l[k-1])


n = int(input())
result(n)

a = [0] * (index[0]+1)
for i in index:
  a[i] = 1
a.reverse()
for i in a:
  print(i, sep='', end='')
      

  