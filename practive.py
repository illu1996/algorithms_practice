import heapq

def dijkstra(G, s):
    q =[]
    heapq.heappush(q,(0,s))
    
    while q:
        
        heapq.heappop()