# 이코테 p312
# 곱하기 혹은 더하기

s = list(map(int,input()))

cnt = 1
ans_num = s[0]

sum_num, bi_num = s[0],s[0]
while  cnt<len(s):
    sum_num = ans_num + s[cnt]
    bi_num = ans_num * s[cnt]
    if sum_num > bi_num:
        ans_num = sum_num
    else:
        ans_num = bi_num
    cnt += 1
    
print(ans_num)