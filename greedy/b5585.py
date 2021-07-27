money = int(input())
receive = 1000-money

list = [500,100,50,10,5,1]
a=0
cnt=0

for value in list:
  if receive < value:
    continue
  cnt=cnt+receive//value
  receive=receive%value
  
print(cnt)