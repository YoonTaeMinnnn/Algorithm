n = int(input())
word = dict()
for _ in range(n):
  word[input()] = 0
wword = [input() for _ in range(n-1)]
for i in wword:
  if word[i] == 0:
    word[i] = 1

for key, value in word.items():
  if value == 0:
    print(key)
    break
  
