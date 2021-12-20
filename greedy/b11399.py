num = int(input())
p = list(map(int,input().split()))

p.sort()

sum=0
realsum=0

for value in p:
  sum+=value  
  realsum+=sum 
print(realsum)