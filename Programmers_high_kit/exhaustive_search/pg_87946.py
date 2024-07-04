# pg 87946
# 피로도

from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    order = list(permutations(dungeons,len(dungeons)))
    # 모든 조합 확인 
    for i in order:
        # 던전 가는 개수
        cnt = 0
        piro = k
        for j in i:
            if piro >= j[0]:
                piro -= j[1]
                cnt += 1
            else:
                break
        if max_count < cnt:
            max_count = cnt
    return max_count

answer = 0

def dfs(k,cnt,dungeons,visit):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(len(dungeons)):
        if k >= dungeons[j][0] and not visit[j]:
            visit[j] = 1
            dfs(k-dungeons[j][1],cnt + 1,dungeons,visit)
            visit[j] = 0
        
def solution(k, dungeons):
    global answer
    n = len(dungeons)
    visit = [0]* n 
    dfs(k,0,dungeons,visit)
    return answer
