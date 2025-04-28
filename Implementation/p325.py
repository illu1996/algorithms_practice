# 자물쇠와 열쇠
# n 자물쇠
# m 열쇠


def solution(key, lock):
    answer = True
    ss = spin(key)
    print(ss)
    return answer

# 회전하기
def spin(key):
    n = len(key)
    newkey = [[0]*n for _ in range(n)]
    # 우측으로 회전하기
    for i in range(n):
        for j in range(n):
            newkey[j][i] = key[i][j]
    return newkey

# 움직이기
def move():
    pass

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])