count = int(input())

case = []
for _ in range(count):
  case.append(int(input()))

moneys = [25,10,5,1]


cnt=0
for i in case:
  money_cnt=[]
  for j in moneys:
    cnt = i//j
    money_cnt.append(cnt)
    print(cnt, end=' ')
    i%=j
  print()

  
  
