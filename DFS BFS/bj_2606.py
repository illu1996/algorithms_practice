# 백준 2606
# 바이러스

#입력
# 컴퓨터 개수 
computer = int(input())
# 연결된 수
node = int(input())

# 0번 제외하고, 1번 부터 n 번까지 list화
connect = [[] for _ in range(computer+1)]

for _ in range(node):
    s,e = map(int,input().split())
    connect[s].append(e)
    connect[e].append(s)

# 같이 0번을 제외하고, 1번부터 n번까지 방문 처리
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

