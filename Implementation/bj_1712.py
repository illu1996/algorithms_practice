# bj 1712 브론즈2
# 손익분기점

a, b, c = map(int,input().split())

# 판매 수 
cnt = 0



# 종료 조건 1 : 제작가가 판매 금액보다 클경우
if c <= b :
    cnt = -1
else:
    cnt = (a//(c-b)) +1
print(cnt)
        