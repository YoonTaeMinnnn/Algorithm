def solution(msg):
answer = []

alpha = {chr(i):i-64 for i in range(65,91)}
num = 27
msg = list(msg)
while msg:
    l = msg.copy()
    c = len(msg)
    while True:
        m = ''.join(l)
        if m in alpha:
            answer.append(alpha[m])
            break
        l.pop()
        c -= 1
    alpha[''.join(msg[:c+1])] = num
    num += 1
    for _ in range(c):
        msg.pop(0)



return answer