from functools import cmp_to_key

n = int(input())
l = list(input().split())
def compare_num(x, y):
  if x+y > y+x:
    return -1
  elif x+y == y+x:
    return 0
  else:
    return 1

l.sort(key = cmp_to_key(compare_num))

cnt = 0
for i in l:
  if i == "0":
    cnt += 1

if cnt == len(l):
  print("0")
else:
  for i in l:
    print(i, sep='', end='')
    
    