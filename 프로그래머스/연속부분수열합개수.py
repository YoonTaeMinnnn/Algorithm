def solution(elements):
    answer = 0
    s = len(elements)
    elements = elements*2
    
    l = set()
    for i in range(1, s+1):
        for j in range(0, s+(i-1)):
            a = elements[j:j+i]
            l.add(sum(a))
            
    return len(l)
    