s = input()
if len(s) == 1:
  print(0)
else:
  cnt = 0
  for i in range(1,len(s)):
    if s[i] != s[i-1]:
      cnt+=1
  print((cnt+1)//2)
  
