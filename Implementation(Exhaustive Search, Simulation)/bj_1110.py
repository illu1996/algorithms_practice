# bj 1110
# 더하기 사이클

import sys
input = sys.stdin.readline

origin = int(input().strip())

# 자리수 판별
def f(n):
    str_n = '0'+ str(n) if len(str(n)) == 1 else str(n)
    return str_n

# 횟수
count = 0
n_num = origin
while 1:
    
    number = f(n_num)
    num = int(number[0]) + int(number[1])
    n_num = str(int(number[1])) + str(num)[-1]
    count += 1
    
    if int(n_num) == origin:
        break
print(count)