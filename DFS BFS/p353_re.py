
# # 이코테 p353
# # 인구이동

n, l, r = map(int,input().split())

human = [list(map(int,input().split())) for _ in range(n)]

# 인구이동 횟수
count = 0

# 4방향
dx= [0,-1,0,1]
dy = [1, 0, -1 ,0]
# 이동해야할 연합 찾는 함수
def find_union():
    union = []
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = dx[k] + i
                ny = dy[k] + j
                
                if 0<= nx <n and 0<= ny < n:
                    if  l<=  abs(human[i][j] - human[nx][ny]) <= r:
                        union.append((i,j))
    if union:
        return tuple(union)
    else:
        return False
    
# 인구 이동
while 1:
    if find_union():
        human_list = list(find_union()) 
        rehuman =0
        for x,y in human_list:
            rehuman += human_list[x][y]
        rehuman //= len(human_list)
        for x,y in human_list:
            human[x][y] = rehuman
        
    else:
        break
    count += 1
    
print(count)
    