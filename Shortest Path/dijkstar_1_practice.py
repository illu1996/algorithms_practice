import sys

input = sys.stdin.readline

INF = int(1e9)

n,m = map(int,input().strip().split())
start = int(input())

G = [[] for _ in range(n+1)]
visited = [0] *(n + 1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().strip().split())
    G[a].append((b,c))
    
# 최단거리 인덱스 반환
def get_smallest_node():
    index= 0
    min_value = INF
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

#다익스트라
def dijkstra(start):
    visited[start] = 1
    distance[start] = 0
    # 시작 노드에서 가장 짧은 거리 찾기
    for j in G[start]:
        distance[j[0]] = j[1]
    # 시작을 제외한 n-1 개 나머지 노드 방문
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = 1
        for j in G[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print(000)
    else:
        print(distance[i])