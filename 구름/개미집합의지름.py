N, D = map(int, input().split())
l = list(map(int, input().split()))

l.sort()
start = 0
end = 0
result = 0
while start < N and end < N:
	if l[end] - l[start] <= D:
		result = max(result, end - start + 1)
		end += 1
	else:
		start += 1

print(N - result)