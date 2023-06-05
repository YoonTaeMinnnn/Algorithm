def solution(number, limit, power):
    def counts(num):
        cnt = 0
        for i in range(1, int((num+1)**(1/2))+1):
            if num % i == 0:
                cnt += 1
                if i**2 != num:
                    cnt += 1
        return cnt
    
    answer = 1
    result = []
    for i in range(2, number + 1):
        c = counts(i)
        
        if c > limit:
            answer += power
        else:
            answer += c
    
        
    return answer