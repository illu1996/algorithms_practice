# 이코테 8-5, p217
# 1로 만들기

# x가 5로 나뉘어지면 나눈다
# x가 3로 나뉘어지면 나눈다
# x가 2로 나뉘어지면 나눈다
# x 에서 1을 뺀다

x = int(input())

#연산 저장
d = [0]*20

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0 :
        d[i] = min(d[i],d[i//2] +1)
    if i % 3 == 0 :
        d[i] = min(d[i],d[i//3] +1)
    if i % 5 == 0 :
        d[i] = min(d[i],d[i//5] +1)
print(d)