# bj 19939
# 박 터뜨리기
# 실버 4

n, k = map(int,input().split())
cnt = 0

def div_n(n,k):
    global cnt
    if sum(list(range(1,k+1))) > n:
        return -1
    else:
        bin = [0] * k
        idx = 0
        while idx <= k:
            bin[idx] = n//k
            idx += 1
            n -= n//k
        # n이 딱 떨