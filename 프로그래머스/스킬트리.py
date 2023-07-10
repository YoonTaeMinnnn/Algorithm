def solution(skill, skill_trees):
    answer = 0
    st = ""
    for skill_tree in skill_trees:
        st = ""
        for s in skill_tree:
           if s in skill:
                st += s
        if skill[:len(st)] == st:
            answer += 1
    

        
    
    return answer