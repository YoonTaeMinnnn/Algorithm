n = int(input())
l = list(map(int, input().split()))
sum = 0
r = 0
for i in l:
  if i == 1:
    r+=1
  else:
    r = 0
  sum+=r  #1 1 2 3 
print(sum)


    