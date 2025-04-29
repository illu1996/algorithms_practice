# 자물쇠와 열쇠
# n 자물쇠
# m 열쇠


def solution(key, lock):
    m = len(key)
    n = len(lock)
    #4방향 회전
    for i in range(4):
        key = spin(key)
    
        # 새로운 자물쇠 만들기
        lenNew = n + (2 * m) -2
        new_lock = [[0] * (lenNew) for _ in range((lenNew))]
        # 새로운 자물쇠에 기존 자물쇠 채우기
        for q in range(m-1, lenNew -(m-1)):
            for w in range(m-1, lenNew -(m-1)):
                new_lock[q][w] = lock[q-(m-1)][w-(m-1)]
        
         # 새로운 자물쇠에 열쇠 넣고 check 하기
        # lenNew 에서 key 길이만큼 빼고 전체 확인

        for a in range(lenNew - m+1):
            for b in range(lenNew - m+1):
                
                check_lock = new_lock
                for x in range(m):
                    for y in range(m):
                        check_lock[a +x][b+y] += key[x][y]
                if check(check_lock,m) == True:
                    return True
                
                for x in range(m):
                    for y in range(m):
                        check_lock[a +x][b+y] -= key[x][y]
    return False

# 회전하기
def spin(key):
    n = len(key)
    newkey = [[0]*n for _ in range(n)]
    # 우측으로 회전하기
    for i in range(n):
        for j in range(n):
            newkey[j][n-1-i] = key[i][j]
    return newkey

# check 하기
def check(new_lock,m):
    for i in range(m-1,len(new_lock) - (m-1)):
        for j in range(m-1,len(new_lock) - (m-1)):
            if new_lock[i][j] != 1:
                return False
    return True
    
solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])