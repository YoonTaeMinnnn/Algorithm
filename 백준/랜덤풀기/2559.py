import sys

input = sys.stdin.readline

n, k = map(int, input().split())
l = list(map(int, input().split()))
result = []
part_sum = sum(l[:k])
result.append(part_sum)

for i in range(n-k):
  part_sum = part_sum - l[i] + l[i+k]
  result.append(part_sum)

print(max(result))