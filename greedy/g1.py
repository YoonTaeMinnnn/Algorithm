n = input()
a = list(map(int,input().split()))
a.sort()

result=0  #그룹의 수
num = 0 # 그룹안의 사람수

for data in a:
  num+=1
  if data <= num:
    result+=1
    num=0

print(result)