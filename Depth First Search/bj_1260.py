# 백준 1260번
# DFS 와 BFS

from collections import deque

#입력
n, m, v = map(int,input().split())
#간선 그래프 변환, 0은 비어두기
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
    
# 작은 번호 부터 출력으로 인한 정렬하기
for i in range(n+1):
    graph[i].sort()

#방문 처리
dfs_visited = [0]*(n+1)
bfs_visited = [0]*(n+1)

def dfs(graph, v, dfs_visited):
    #방문처리
    dfs_visited[v] = 1
    print(v, end=" ")
    #이어진 노드 재귀를 이용한 탐색
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(graph, i,dfs_visited)
            
dfs(graph, v, dfs_visited)
print()

def bfs(graph, v, bfs_visited):
    q = deque([v])
    bfs_visited[v] = 1
    while q:
        v=q.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not bfs_visited[i]:
                bfs_visited[i] = 1
                q.append(i)

bfs(graph, v, bfs_visited)