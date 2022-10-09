l = [list(map(int, input().split())) for _ in range(7)]

result = 0

for i in range(7):
  sub = l[i].copy()
  subb = [j[i] for j in l]
  for z in range(3):
    cnt = 0
    cntt = 0
    a = sub[z:z+5]
    b = subb[z:z+5]
    for w in range(2):
      if a[w] == a[-1-w]:
        cnt += 1
      if b[w] == b[-1-w]:
        cntt += 1
    if cnt == 2:
      result += 1
    if cntt == 2:
      result +=1

print(result)
  

