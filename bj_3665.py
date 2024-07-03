# bj 17470
# 배열 돌리기

n, m, r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
order = list(map(int,input().split()))

# 1번 연산
def f1(n,arr):
    new_arr = [[] for _ in range(n)]
    
    for i in range(n-1,-1,-1):
        new_arr[n-i-1] = arr[i]
    return new_arr

def f2(n,arr):
    new_arr = [[] for _ in range(n)]
    
    for i in range(n):
        new_arr[i] = arr[i].reverse
    return new_arr

def f3(n,m,arr):
    new_arr = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[m-j][i]
    return new_arr
        
answer = []
for i in order:
    if i ==3:
        answer = f3(n,m,arr)

for i in range(n):
    print(answer[i])

# 00 01 02 03 04 05
# 50 40 30 20 10 00