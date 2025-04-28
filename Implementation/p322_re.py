# 문자열 재정렬

s = list(input())
s.sort()
rst = ''
sumnum = 0
for i in s:
    if i.isnumeric():
        sumnum += int(i)
    else:
        rst += i

print(rst + str(sumnum))