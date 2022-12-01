def result(n):
  if n == 0:
    return
  result(n//2)
  print(n%2, end='')

n = int(input())
result(n)