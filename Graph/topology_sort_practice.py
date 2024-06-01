# 위상 정렬
from collections import deque

v, e = map(int,input().split())
indegree = [0]*(v+1)
G = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input())
    G[a].append(b)
    indegree[b] +=1

#위상정렬

def topology_sort():
    result = []
    q = deque([])
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in G[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            
    for i in result:
        print(i, end=" ")
topology_sort()
