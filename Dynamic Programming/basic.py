#이코테 

#피보나치 기본
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))


#피보나치(재귀) == 탑다운 == 하향식 == 메모이제이션
d = [0]*100
def fibo1(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo1(x-1) + fibo1(x-2)
    return d[x]
print(fibo1(99))

#피보나치(반복문) == 바텀업 == 상향식
d = [0]*100
d[1] = 1
d[2] = 1
n=99
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])