ques = input().split('-')
cnt=0
result = 0

for i in ques:
  sub_list = i.split('+')
  int_list=[]
  for i in sub_list:
    int_list.append(int(i))
  if cnt==0:
    result=sum(int_list)
    cnt+=1
  else:
    result-=sum(int_list)

        
print(result)
