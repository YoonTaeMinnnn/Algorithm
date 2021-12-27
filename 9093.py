n = int(input())

seq_list = []
for _ in range(n):
  seq_list.append(list(input().split()))
for seq in seq_list:
  for i in seq:
    new_word = list(i)
    new_word.reverse()
    print("".join(map(str, new_word)),'', end='')
  print()