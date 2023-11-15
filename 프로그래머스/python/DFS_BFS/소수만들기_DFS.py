def solution(nums):
    global answer
    answer = 0
    def counts(com):
        for i in range(2, int(com**(1/2))+1):
            if com % i == 0:
                return 1
        return 0
    
    def DFS(L, s, b):
        global answer
        if L == 3:
            if counts(s) == 0:
                answer += 1
        else:
            for i in range(n):
                if i > b:
                    DFS(L+1, s+nums[i], i)
                    
    
    n = len(nums)
    ch = [0] * n
    DFS(0,0,-1)
    

    return answer