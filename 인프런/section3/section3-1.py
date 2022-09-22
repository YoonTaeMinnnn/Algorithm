n = int(input())
for i in range(1,n+1):
  word = input()
  word = word.lower()
  if word == word[::-1]:
    print('#%d YES' %i)
  else:
    print('#%d NO' %i)
    