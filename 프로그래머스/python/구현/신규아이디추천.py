def solution(new_id):
    new_id = new_id.lower()
    sample = ['0','1','2','3','4','5','6','7','8','9','-','_','.']
    for i in new_id:
        if i.islower():
            continue
        if i not in sample:
            new_id = new_id.replace(i,'')
    
    while '..' in new_id:
        new_id = new_id.replace('..','.')
    
    
    if new_id[0] == '.':
        if len(new_id)>=2:
            new_id = new_id[1:] 
        else:
            new_id = '.'
    if new_id[-1]=='.':
        new_id = new_id[:-1]
    
    if new_id=='':
        new_id = 'a'
    
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1]=='.':
            new_id = new_id[:-1]
    
    
    while len(new_id) < 3 :
        new_id+=new_id[-1]
    answer = new_id
    return answer