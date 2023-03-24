n = int(input())
l = list(map(int, input().split()))

result = []
last = 0
lt = 0
rt = n - 1
res = ""

while lt <= rt:
  if l[lt] > last:
    result.append((l[lt], "L"))
  if l[rt] > last:
    result.append((l[rt], "R"))
  if len(result) == 0:
    break
  else:
    l.sort()
    res += result[0][1]
    last = result[0][0]
    if result[0][1] == "L":
      lt += 1
    else:
      rt -= 1
  result.clear()
    
  
  