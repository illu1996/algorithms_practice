# 럭키스트레이트
n = list(map(int,input()))
half = len(n)//2

first = n[0:half]
last = n[half:len(n)]

if sum(first) == sum(last):
    print("LUCKY")
else:
    print("READY")