n = int(input())
for _ in range(n):
  a = list(input())
  result = 0
  now = 0
  for i in a:
    if i=='O':
      if now > 0:
        now = now + 1
        result = result + now 
        continue
      now = now + 1
      result = result + now
      continue
    now = 0
  print(result)

    

      