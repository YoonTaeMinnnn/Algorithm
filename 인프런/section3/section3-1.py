#---------슬라이싱 이용---------
n = int(input())
for i in range(1,n+1):
  word = input()
  word = word.lower()
  if word == word[::-1]:
    print('#%d YES' %i)
  else:
    print('#%d NO' %i)

#----직접 구현------

n = int(input())
for i in range(1,n+1):
  word = input()
  word = word.lower()
  index = len(word) // 2
  for j in range(index):
    if word[j] != word[-1-j]:
      print('#%d NO' %i)
      break
  else:
    print('#%d YES' %i)
  
    