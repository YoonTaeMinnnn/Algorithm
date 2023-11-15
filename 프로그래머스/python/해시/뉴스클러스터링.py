def solution(str1, str2):
    answer = 0
    
    d1 = dict()
    d2 = dict()
    
    for i in range(len(str1)-1):
        if not str1[i].isalpha() or not str1[i+1].isalpha():
            continue
        s = str1[i].lower() + str1[i+1].lower()
        d1[s] = d1.get(s, 0) + 1
    
    for i in range(len(str2)-1):
        if not str2[i].isalpha() or not str2[i+1].isalpha():
            continue
        s = str2[i].lower() + str2[i+1].lower()
        d2[s] = d2.get(s, 0) + 1
    
    s1 = list(d1.keys())
    s2 = list(d2.keys())
    
    a = 0
    for i in s1:
        if i in s2:
            a += min(d1[i], d2[i])
            
    b = sum(list(d1.values())) + sum(list(d2.values())) - a
    
    if a == 0 and b == 0:
        return 65536
    
    answer = int((a / b) * 65536)
    
    return answer