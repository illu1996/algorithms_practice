# 다익스트라

import sys
input = sys.stdin.readline
INF = 1e9

n, m = map(int,input().split())
visited = [0] * (n+1)
distance = [INF] * (n+1)
s = int(input())
G = [[] for _ in range(n+1)]
for i in range(n):
    a,b,c = map(int,input().split())
    G[a].append((b,c))

# 최단거리의 노드 찾는 함수
def small():
    min_val = INF
    index = 0
    # 시작을 제외한 방문하지 않은 노드들 중
    for i in range(1,n+1):
        if distance[i] < min_val and visited[i]:
            min_val = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(s):
    visited[s] = 1
    distance[s] = 0
    # 시작 노드로부터의 최단거리 설정
    for j in G[s]:
        distance[j[0]] = j[1]
    # 시작을 제외한 모든 노드 방문
    for i in range(n-1):
        now = small()
        visited[now] = 1
        # 노드 들의 거리값 확인
        for j in G[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost