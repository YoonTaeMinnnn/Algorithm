def hourse(m):
    a = l[0]
    cnt = 1
    for i in range(1, n):
        if l[i] - a >= m:
            a = l[i]
            cnt += 1
    if cnt < c:
        return False
    return True


n, c = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()
lt = 1
rt = l[n - 1]
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if hourse(mid):
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
