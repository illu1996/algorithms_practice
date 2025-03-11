# 백준 14891 골드5
# 톱니바퀴

# 시계방향 회전 함수
def right_spin(arr):
    num = arr.pop()
    arr.insert(0,num)
# 반시계 방향 회전함수
def left_spin(arr):
    num = arr.pop(0)
    arr.append(num)

# 12시 방향 톱니 점수 판단
def score(idx):
    if idx == 0 and top[0][0] == 1:
        return 1
    elif idx == 1 and top[1][0] == 1:
        return 2
    elif idx == 2 and top[2][0] == 1:
        return 4
    elif idx == 3 and top[3][0] == 1:
        return 8
    return 0

top = []
for i in range(4):
    top.append(list(map(int,list(input()))))

# 12시부터 시계방향으로 n극 0, s극 1

# 회전횟수 k
k = int(input())

for i in range(k):
    s_num, s_d = map(int,input().split())
    
    d= s_d
    left_n = 0
    right_n = 3
    flag = True
    
    # 우선 돌려
    if s_d == 1:
        right_spin(top[s_num-1])
    elif s_d == -1:
        left_spin(top[s_num-1])
    
    num = s_num
    # 내 톱니 돌릴때 양 옆에 확인하기
    # 오른쪽 확인
    while num <= right_n:
        right = top[num-1][2]
        if  num <= 3 and right != top[num][6]:
            if d == 1:
                left_spin(top[num])
                d = -1
                num += 1
                continue
            elif d == -1:
                right_spin(top[num])
                d = -1
                num += 1
                continue
        else:
            break
            
    num = s_num -2
    d= s_d
    # 왼쪽 계속 확인
    while num >= left_n:
        
        left = top[num+1][6]
        if  num - 2  >= 0 and left != top[num][2] :
            if d == 1:
                left_spin(top[num])
                d = -1
                num -= 1
                continue
            elif d == -1:
                right_spin(top[num])
                d = 1
                num -= 1
                continue
        else:
            break
            
# 출력
ans = 0
for i in range(4):
    ans += int(score(i))
print(ans)