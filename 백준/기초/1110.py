n = int(input())
count = 0
result = n
while True:
  f = result // 10
  s = result % 10
  result = s*10 + (f+s)%10
  count = count + 1
  if result == n:
    break
  
print(count)
  