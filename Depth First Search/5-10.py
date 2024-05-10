
# 이것이 취업을 위한 코딩 테스트다

# 음료수 얼려 먹기 p149

# 첫째줄 입력
n,m = map(int,input().split())
# 얼음 입력
ice = [list(map(int, input())) for _ in range(n)]

# dfs 정의
def dfs(x,y):
    #갈 필요 없는 조건
    if x< 0 or x>=n or y <0 or y>=m:
        return False
    if ice[x][y]==0:
        ice[x][y] = 1
        # 상하 좌우 이동
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False

count = 0
# 방향 탐색               
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count += 1
            
print(count)
