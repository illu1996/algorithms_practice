import sys
# baekjoon 10828

# 구현

# 스택 박스
stack_box = []

n = int(input())
for i in range(n):
    result = sys.stdin.readline().split()
    if result[0] == 'push':
        stack_box.append(result[1])
    elif result[0] == 'pop':
        if len(stack_box ) == 0:
            print(-1)
        else:
            print(stack_box [-1])
            stack_box.pop()
    elif result[0] == 'size':
        print(len(stack_box ))
    elif result[0] == 'empty':
        if len(stack_box ) == 0:
            print(1)
        else:
            print(0)
    elif result[0] == 'top':
        if len(stack_box ) == 0:
            print(-1)
        else:
            print(stack_box [-1])
