#백준 단어뒤집기2 17413
# 실버 3

# 단어라면 스택에
# 아니라면 바로 추가해주기

from collections import deque
s = list(input())
s.append(' ')

stack = []
res = ''
is_cell = 0 #괄호 안에 있는지 판단하기

for i in list(s):
    # 공백이고 괄호 아니라면 스택에서 모든 단어 빼주기
    if i == ' ' and is_cell ==0:
        while stack:
            res += stack.pop()
        res += ' '
    # 괄호 시작이라면 괄호모드 체크, 스택에 있는 단어 모두 빼기
    if i =='<':
        is_cell = 1
        
        while stack:
            res += stack.pop()
    # 괄호 끝이라면 괄호모드 끄고 추가해주고 바로 컨티뉴
    if i == '>':
        is_cell = 0
        res += '>'
        continue
    
    # 괄호모드라면 바로추가
    if is_cell:
        res += i
    elif i != " " and is_cell ==0:
        stack.append(i)

res.strip()
print(res)