from collections import deque

def dfs():
    visited[v] = 1
    
    for i in G[v]:
        if not visited[i]:
            dfs(i)
    stack = [v]
    visited[v] = 1
    v = stack.pop()
    for i in G[v]:
        if not visited[i]:
            
            stack.append(i)