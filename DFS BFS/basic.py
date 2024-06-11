# DFS 깊이우선 탐색

def dfs1(G,v,visited):
    visited[v] = 1
    print(v,end=' ')
    for i in G[v]:
        if not visited[i]:
            dfs1(G,i,visited)

G = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
visited = [0]*len(G)

# dfs1(G,1,visited)

def dfs2(G,v,visited):
    stack = []
    stack.append(v)
    visited[v] = 1
    while stack:
        now = stack.pop()
        print(now, end=' ')
        for i in G[now]:
            if not visited[i]:
                visited[i]=  1
                
                stack.append(i)

dfs2(G,1,visited)

# bfs 넓이 우선 탐색
from collections import deque
def bfs(G,v,visited):
    q = deque([v])
    visited[v] = 1
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in G[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                
# bfs(G,1,visited)