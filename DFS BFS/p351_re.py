n = int(input())

school = [list(map(str,input().split())) for _ in range(n)]

# 선생님 위치
T_location = []
for i in range(n):
    for j in range(n):
        if school[i][j] == 'T':
            T_location.append((i,j))
# 감시망 
def check_T(x,y,direction):

    if direction == 0:
        while y>=0:
            if school[x][y] =='S':
                return True
            if school[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if school[x][y] =='S':
                return True
            if school[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x>=0:
            if school[x][y] =='S':
                return True
            if school[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x< n:
            if school[x][y] =='S':
                return True
            if school[x][y] == 'O':
                return False
            x+= 1

    return False
result = False
# 벽 세우기
count = 0
for i in range(n):
    for j in range(n):
        if school[i][j] == "X":
            school[i][j] = 'O'
            count +=1
            if count == 3:
                for x,y in T_location:
                    for k in range(4):
                        if not check_T(x,y,i):
                            result = True
                            break
            count -=1
            school[i][j] ='X'
        if result:
            break
    if result:
        braek

if result==False:
    print('NO')
else:
    print('YES')