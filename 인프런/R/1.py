n = int(input())
words= []
for _ in range(n):
  words.append(input().lower())

for i in range(len(words)):
  if words[i][::-1] == words[i]:
    print("#",i+1," YES", sep='')
  else:
    print("#",i+1," NO", sep='')

  
    