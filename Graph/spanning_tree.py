# 신장 트리
# 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 그래프

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a= find_parent(parent, a)
    b= find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int,input().split())
parent  = [0]*(v+1)

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += cost
print(result)
    