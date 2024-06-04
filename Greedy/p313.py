# 이코테 p 313
# 문자열 뒤집기

s = input()

cnt_one = 0
cnt_zero = 0
#1로 만들기
for i in range(1,len(s)):
    if s[0] =='0':
        cnt_one +=1
    if s[i-1] =='1' and s[i]=='0':
        cnt_one += 1

#0로 만들기
for i in range(1,len(s)):
    if s[0] == '1':
        cnt_zero += 1
    if s[i-1] == '0' and s[i] =='1':
        cnt_zero +=1
        
print(min(cnt_zero,cnt_one))