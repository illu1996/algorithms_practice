# bj 17470
# 배열 돌리기
import sys
input = sys.stdin.readline

def f1(n,arr):
    new_arr = [[] for _ in range(n)]
    
    for i in range(n-1,-1,-1):
        new_arr[n-i-1] = arr[i]
    return new_arr

def f2(n,arr):
    new_arr = []

    for i in range(n):
        new_row = list(reversed(arr[i]))
        new_arr.append(new_row)
    return new_arr

def f3(n,m,arr):
    new_arr = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[n-1-j][i]
    return new_arr

def f4(n,m,arr):
    new_arr = [[0]*n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            new_arr[i][j] = arr[j][m-1-i]
    return new_arr

def f5(n,m,arr):
    
    new_n = n//2
    new_m = m//2
    all_1 = arr[:new_n]
    all_2 = arr[new_n:n]
    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []
    for i in range(len(all_1)):
        arr_1.append(all_1[i][:new_m])
        arr_2.append(all_1[i][new_m:m])
        arr_4.append(all_2[i][:new_m])
        arr_3.append(all_2[i][new_m:m])
    new_arr = []

    for i,j in zip(arr_4,arr_1):
        new_row = i+j
        new_arr.append(new_row)
    for i,j in zip(arr_3,arr_2):
        new_row= i +j
        new_arr.append(new_row)
    return new_arr

def f6(n,m,arr):
    
    new_n = n//2
    new_m = m//2
    all_1 = arr[:new_n]
    all_2 = arr[new_n:n]
    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []
    for i in range(len(all_1)):
        arr_1.append(all_1[i][:new_m])
        arr_2.append(all_1[i][new_m:m])
        arr_4.append(all_2[i][:new_m])
        arr_3.append(all_2[i][new_m:m])
    new_arr = []

    for i,j in zip(arr_2,arr_3):
        new_row = i+j
        new_arr.append(new_row)
    for i,j in zip(arr_1,arr_4):
        new_row= i +j
        new_arr.append(new_row)
    return new_arr

n, m, r = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
order = list(map(int,input().split()))


for i in order:
    if i ==1:
        arr = f1(n,arr)
    elif i ==2:
        arr = f2(n,arr)
    elif i ==3:
        arr = f3(n,m,arr)
        n, m = m, n
    elif i ==4:
        arr = f4(n,m,arr)
        n, m = m, n
    elif i ==5:
        arr = f5(n,m,arr)
    else:
        arr = f6(n,m,arr)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end = ' ')
    print()
        
        

# 00 01 02 03 04 05
# 50 40 30 20 10 00