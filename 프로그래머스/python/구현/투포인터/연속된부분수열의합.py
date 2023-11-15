def solution(sequence, k):
    answer = []
    
    left = 0
    right = 0
    s = sequence[left]

    stack = []
    
    while True:
        if s < k:
            right += 1
            if right == len(sequence):
                break
            s += sequence[right]
        elif s > k:
            s -= sequence[left]
            left += 1
        elif s == k:
            s -= sequence[left]
            stack.append([left, right])
            left += 1
    
    stack.sort(key = lambda x : (x[1]-x[0], x[0]))
        
    return stack[0]