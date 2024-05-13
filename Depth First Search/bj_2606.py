# 백준 2606
# 바이러스

#입력
computer = int(input())
node = int(input())

connect = [[] for _ in range(computer+1)]

for _ in range(node):
    s,e = map(int,input().split())
    connect[s].append(e)
    connect[e].append(s)

    
visited = [0]*(computer+1)

count = 0
def dfs(connect, v, visited):
    global count
    visited[v] = 1
    for i in connect[v]:
        if not visited[i]:
            visited[i] = 1
            count += 1
            dfs(connect, i, visited)
    

dfs(connect, 1,visited)
print(count)