#백준 단어뒤집기2 17413
# 실버 3

from collections import deque
s = list(input())
stack = []
q = deque([])
res = ''

cnt = 0

while True:
    if cnt == len(s):
        break
    if s[cnt] == '<':
        res += '<'
        cnt += 1
        while True:
            if s[cnt] != '>':
                res += s[cnt]
                cnt += 1
            elif s[cnt] ==  '>':
                res += '>'
                res += '>'
                cnt += 1
                break
        q.append(res)
    
    elif s[cnt] ==' ':pass
    
    else:
        stack.append(s[cnt])
        
        
        