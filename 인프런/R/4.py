n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

result = n_list + m_list
result.sort()
print(*result)
  