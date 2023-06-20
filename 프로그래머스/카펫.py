def solution(brown, yellow):
    answer = []
    l = []
    y = []
    total = brown + yellow
    # (1,12), (2,6), (3,4)
    for i in range(1, int(total**(1/2))+1):
        if total % i == 0:
            com = total // i
            if com >= i:
                l.append((com, i))
            else:
                l.append((i,com))
    
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            com = yellow // i
            if com >= i:
                y.append((com, i))
            else:
                y.append((i,com))

    
    for i in range(len(l)):
        for j in range(len(y)):
            if l[i][0] > y[j][0]+1 and l[i][1] > y[j][1]+1:
                return l[i]
            
    return answer








