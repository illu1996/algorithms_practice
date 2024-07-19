# pg 86971
# 전력망을 둘로 나누기
# 레벨 2

from collections import deque

def bfs(G, visit,start):
    # 시작되면서 노드 개수 1
    cnt = 1
    q = deque([])
    visit[start] = 1
    q.append(start)
    while q:
        now = q.popleft()
        for i in G[now]:
            if not visit[i]:
                visit[i] =1
                #방문 가능할때마다 연결된 노드 개수 추가
                cnt += 1
                q.append(i)
    return cnt

def solution(n, wires):

    
    min_val = 100
    
    #자른 와이어를 제거하고 완전탐색
    for i in range(0,n-1):
        visit = [0] * (n+1)
        
        G = [[] for _ in range(n+1)]
        renew = wires[0:i] + wires[i+1:n]
        for a,b in renew:
            G[a].append(b)
            G[b].append(a)
        # print(G)
        
        #연결되어 있는 노드 개수
        result = []
        #방문 확인하면서 bfs
        for j in range(1,len(visit)):

            if visit[j] == 0:
                result.append(bfs(G,visit, j))
        # print(result)
        
        # 노드 개수 차이 바꿔주기
        abs_val = abs(result[0] - result[1])
        if min_val > abs_val:
            min_val = abs_val
        
            
    return min_val

'''
9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
3
4, [[1,2],[2,3],[3,4]]
0
7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
1
'''