# pg 42587
# 프로세스

def solution(priorities, location):
    answer = []
    num = list(enumerate(priorities))
    q = num
    ans=''

    while q:
        i,order = q.pop(0)
        
        for k,o in q:
            if order < o:
                q.append((i,order))
                break
        else:
            answer.append((i,order))    
            
    for i in range(len(answer)):
        if location == answer[i][0]:
            ans = i + 1
    return ans
