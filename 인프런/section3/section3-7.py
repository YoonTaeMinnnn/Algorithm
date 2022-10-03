n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
su = 0
k = n // 2
s = n // 2
c = n // 2 + 1
for i in range(n):
    if i <= k:
        sub = l[i][s:i + c]
        su += sum(sub)
        s -= 1
        if i == k:
            s += 1
    else:
        s += 1  # i = 4, s = 2
        sub = l[i][s:n + k - i]
        su += sum(sub)

print(su)

#10 13 10 12 15 /12 39 30 23 11 /11 25 50 53 15 /19 27 29 37 27 /19 13 30 13 19
