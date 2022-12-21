from itertools import permutations

# n, m = map(int, input().split())
# ch = [0] * (n+1)
# b = [1] * n
# for i in range(1, n):
#   b[i] = b[i-1] * (n-i) // i
# p = [0] * n

a = [i for i in range(1,5)]
for tmp in permutations(a):
  print(tmp)