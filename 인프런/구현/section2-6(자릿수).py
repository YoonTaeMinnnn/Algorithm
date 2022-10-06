n = int(input())
digit = list(map(int, input().split()))


def digit_sum(x):
  sum = 0
  while x > 0:
    sum+=x%10
    x//=10
  return sum


result = []
for i in digit:
    result.append(digit_sum(i))
max_result = max(result)
for i in range(n):
    if result[i] == max_result:
        print(digit[i])
        break
