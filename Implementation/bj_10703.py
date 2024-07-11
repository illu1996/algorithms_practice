# bj 10703
# 유성

n, m = map(int,input().split())
maps = [list(input()) for _ in range(n)]
all_star = []

air = [0] * m
star = [0] * m

# 유성 맨 아래부분 찾기
for i in range(m):
    for j in range(n-1,-1,-1):
        if maps[j][i] == 'X':
            star[i] = (j,i)
            break

# 땅 맨 윗 부분 찾기
for i in range(m):
    for j in range(n):
        if maps[j][i] == '#':
            air[i] = (j-1,i)
            break

# n 값 찾기
def f(arr,arr1,n):
    while n > 0:
        flag = 1
        for i in range(m):
            if arr[i] == 0:
                continue
            else:
                if arr1[i][0] - arr[i][0] >= n:
                    continue
                else:
                    flag = 0
                    break
        if flag == 1:
            return n
        else:
            n -=1
    return 
answer = f(star,air,n)

# 유성찾기(거꾸로 탐색)
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if maps[i][j] =='X' and 0<= i+answer < n and maps[i+answer][j] == '.':
            maps[i+answer][j] = 'X'
            maps[i][j] = '.'

for i in range(n):
    print(''.join(maps[i]))

