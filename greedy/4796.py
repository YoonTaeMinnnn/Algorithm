result_list=[]
while True:
  result = 0
  l,p,v = map(int, input().split())
  if l==0 and p==0 and v==0:
    break
  result += (v // p)*l
  result+=min(v%p,l)
  result_list.append(result)

for i in range(len(result_list)):
  print('Case ',i+1,': ',result_list[i], sep='')

  
