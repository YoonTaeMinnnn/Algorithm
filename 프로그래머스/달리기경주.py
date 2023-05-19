def solution(players, callings):
    a = {v:k for k, v in enumerate(players)}
    
    for call in callings:
        now = a[call]
        pre = players[now-1]
        players[now-1] = call
        players[now] = pre
        a[call] -= 1
        a[pre] += 1
    
    return players
            
    