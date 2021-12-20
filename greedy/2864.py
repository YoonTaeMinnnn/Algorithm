a,b = map(int,input().split())
a= str(a)
b=str(b)

if '5' in a or '5' in b:
  a_sub = a.replace('5','6')
  b_sub = b.replace('5','6')
  max = int(a_sub) + int(b_sub)
else :
  max = int(a)+ int(b) 

if '6' in a or '6' in b:
  a_sub = a.replace('6','5')
  b_sub = b.replace('6','5')
  min = int(a_sub) + int(b_sub)
else:
  min = int(a)+int(b)

print(min,max)
