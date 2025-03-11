# 백준 1543 문서검색
# 실버 5

s = input()
fs = input()

# 문자열이 있으면 시작 인덱스부터 끝인덱스까지 제거 하고 카운트를 올린다

cnt = 0
index = 0
# while index <= len(s):
#     if fs in s:
#         cnt += 1
#         index = len(fs)
#         s = s[index:]

#     else:
#         index += 1
#         s = s[index:]
#     index = 0
# print(cnt)

while index < len(s):
    flag = 0
    sum_index = 0
    for i in fs:
        if index < len(s) and i == s[index]:
            flag = 1
            index += 1
            sum_index += 1
        else:
            flag = 0
    index -= sum_index
    if flag:
        cnt += 1
        flag = 0
        index += len(fs)
    else :
        index += 1
print(cnt)