# 연습장

# dfs
from collections import deque

def dfe(G, v, visited):
    visited[v] = 1
    
    for i in G[v]:
        if not visited:
            visited[i] = 1
            dfe(G, i, visited)
            
def bfs(G, v, visited):
    q = deque([v])
    visited[v] = 1
    while q:
        now = q.popleft()
        for i in G[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)