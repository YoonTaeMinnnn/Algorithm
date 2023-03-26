second = int(input())

# // 몫만 출력
a = second // 300
second%=300
b = second // 60
second%=60
c = second // 10
second%=10

if second != 0:
  print(-1)
else:
  print(a,b,c)