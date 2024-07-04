# pg 12909
# 올바른 괄호

def solution(s):
    stack = []
    
    # 처음시작이 닫는거면 바로 탈출
    if s[0] == ')':
        return False
    else:
        stack.append(s[0])
    
    # ')'면 빼주기
    for i in range(1,len(s)):
            
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not len(stack):
                return False
            else:
                stack.pop()
        
    # stack 길이가 0 = True
    if not len(stack):
        return True
    else:
        return False