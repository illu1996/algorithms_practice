import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int,input().strip().split())
start = int(input())
G = [[] for _ in range(n+1)]
visited = [0] * (n+1)
distance = [INF] * (n+1)


for _ in range(m):
    a,b,c = map(int, input().strip().split())
    G[a].append((b,c))
    
print(G)
print(visited)
print(distance)
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in G[start]:
        distance[j[0]] = j[1]
        
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in G[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])