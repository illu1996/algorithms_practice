# 외벽 점검

# n 외벽 길이 200
# weak 취약지점 위치 15
# 1시간 동안 이동할 수 있는 dist
# 시계 / 반시계

from itertools import permutations

def solution(n, weak, dist):
        
    # 사람 수 늘려 가면서

        # 투입 위치 바꾸면서??
        # == 문제의 최장 거리를 알면 쉬움
        # == 문제들의 거리를 최소로 만들고 합을 구하면 됌
        
        # 1. n 의 거리를 가진 친구가 있다면 바로 1명
        # 2. m명을 투입했을때의 문제 m 명이 커버할 수 있는 거리를 구해야함
    if n in dist:
        return 1    
    else:
        # m명 투입l
        for i in range(2,len(dist)+1):
            friends = list(permutations(dist,i))
            for j in friends:
                

    
solution(12, [1,5,6,10], [1,2,3,4])

