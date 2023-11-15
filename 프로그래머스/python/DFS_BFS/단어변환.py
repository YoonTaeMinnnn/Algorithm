from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    def count(com1, com2):
        cnt = 0
        for i in range(len(com1)):
            if com1[i] != com2[i]:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False
    
    queue = deque()
    queue.append((begin, 0))
    visited = [0] * len(words)
    while queue:
        word, num = queue.popleft()
        if word == target:
            answer = num
            break
        else:
            for i in range(len(words)):
                if visited[i] == 0:
                    if count(word, words[i]):
                        visited[i] = 1
                        queue.append((words[i], num+1))
            
    return answer