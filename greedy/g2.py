#거스름돈문제1-1

money = int(input()) #5000
cnt=0

m = [500,100,50,10]

for i in m:
  cnt += money//i
  money %= i

print(cnt)
