def solution(n, k):
    answer = 0
    
    # 소수 구하기 
    def count(n):
        if n == 1:
            return False
        cnt = 0
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                cnt += 1 
        if cnt > 0:
            return False
        return True
    
    def change(n):
        rev_base = ''
        while n > 0:
            n, mod = divmod(n, k)
            rev_base += str(mod)
        return rev_base[::-1] 
    
    num = change(n)
    
    s = ''
    stack = []
    cnt = 0
    cmt = 0
    for i in range(len(num)):
        if int(num[i]) != 0:
            if cmt == 0:
                start = i
            s += num[i]
            cnt = 0
            cmt += 1
        elif cnt == 0:
            end = i-1
            stack.append([start, end])
            s = ''
            cnt += 1
            cmt = 0
            
    if cmt != 0:
        stack.append([start, len(num)-1])
    
    for i in stack:
        if count(int(num[i[0]:i[1]+1])):
            answer += 1
    

    return answer