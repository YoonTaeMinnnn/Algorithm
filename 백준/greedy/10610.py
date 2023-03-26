n = int(input())

test_n = str(n)
int_list = []
batch_list = []


if '0' not in str(n):
  print(-1)
else: 
  zero_count = str(n).count('0')
  test_n = str(n).replace('0','')
  if int(test_n)%3 !=0:
    print(-1)
  else:
    test_list = list(test_n)
    for i in test_list:
      batch_list.append(int(i))
    batch_list.sort(reverse=True)
    for _ in range(zero_count):
      batch_list.append(0)
    str_list = list(map(str,batch_list))
    result = "".join(str_list)
    print(int(result))


