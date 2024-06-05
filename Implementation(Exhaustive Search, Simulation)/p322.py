#이코테 p322
# 문자열 재정렬

s = list(input())
s.sort()

count = 0
for i in range(len(s)):
    if s[i].isdigit():
        count += int(s[i])
    
new_s = list(filter(lambda x:x.isalpha() == True,s ))

new_s.append(str(count))

print(''.join(new_s))