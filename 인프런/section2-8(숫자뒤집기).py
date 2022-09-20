n = int(input())
l = list(map(int, input().split()))
r = []


def reverse(x):
  return int(str(x)[::-1])
  

def isPrime(x):
  if x == 1:
    return False
  for i in range(2,x):
    if x % i ==0:
      return False
  return True

for i in l:
  r.append(reverse(i))

for i in r:
  if isPrime(i):
    print(i, end=' ')
