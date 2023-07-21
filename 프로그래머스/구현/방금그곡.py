def solution(m, musicinfos):
    answer = ''
    stack = []
    index = 0
    def change(n):
        if "A#" in n:
            n = n.replace("A#", "a")
        if "C#" in n:
            n = n.replace("C#", "c")
        if "D#" in n:
            n = n.replace("D#", "d")
        if "F#" in n:
            n = n.replace("F#", "f")
        if "G#" in n:
            n = n.replace("G#", "g")
        return n
    
    m = change(m)
    print(m)
    
    for music in musicinfos:
        index += 1
        start = music.split(',')[0]
        end = music.split(',')[1]
        title = music.split(',')[2]
        flow = music.split(',')[3]
        flow = change(flow)
        flow_len = len(flow)
        play_time_len = (int(end.split(':')[0]) * 60 + int(end.split(':')[1])) - (int(start.split(':')[0])*60 + int(start.split(':')[1]))
        
        play = flow * (play_time_len // flow_len) + flow[:play_time_len % flow_len]
        
        if m in play:
            stack.append((len(play), index, title))
        
            
    if not stack:
        return "(None)"
    elif len(stack) == 1:
        return stack[0][2]
    else:
        stack.sort(key = lambda x : (-x[0], x[1]))
    return stack[0][2]