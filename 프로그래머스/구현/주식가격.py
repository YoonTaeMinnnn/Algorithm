def solution(prices):
    answer = []
    s = len(prices)
    
    for i in range(s):
        cnt = 0
        for j in range(i+1, s):
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    
        
    return answer