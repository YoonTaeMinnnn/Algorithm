def solution(s, skip, index):
    answer = ''
    
    for word in s:
        cnt = 0
        while index > cnt:
            if ord(word) + 1 > 122:
                word = 'a'
            else:
                word = chr(ord(word) + 1)
            if word in skip:
                continue
            else:
                cnt += 1
        answer += word        
    return answer