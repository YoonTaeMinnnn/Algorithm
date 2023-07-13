def solution(numbers, target):
    size = len(numbers)
    def DFS(L, s):
        global cnt
        if L == size:
            if s == target:
                cnt += 1
        else:
            DFS(L+1, s+numbers[L])
            numbers[L] = numbers[L] * -1
            DFS(L+1, s+numbers[L])
    global cnt
    cnt = 0
    DFS(0,0)
    print(cnt)
    return cnt;
