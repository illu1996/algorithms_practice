# 이코테 #p390
# 숨바꼭질
import heapq
n, m= map(int,input().split())
s =1
INT = 1e9
G = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

    
distance = [INT]*(n+1)
q = []
heapq.heappush(q,(0,1))
distance[0] = 0
distance[1] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in G[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q,(cost,i))
            
max_val = max(distance)
index = -1

for i in range(1,n+1):
    if distance[i] == max_val:
        index = i
        break
count= distance.count(max_val)    

print(index, max_val, count)
    