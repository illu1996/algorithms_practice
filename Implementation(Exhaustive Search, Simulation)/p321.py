# 이코테 p321
# 럭키 스트레이트

n = list(map(int,input()))

pivot = len(n) //2

left_sum = sum([ n[i] for i in range(0,pivot)])
right_sum = sum([n[i] for i in range(pivot,len(n))])

if left_sum == right_sum:
    print('LUCKY')
else:
    print("READY")

