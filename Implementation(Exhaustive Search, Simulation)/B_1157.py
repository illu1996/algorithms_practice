
# baekjoon 1157

# 구현 

# 입력받은 단어
word = list(input())

# A ~ Z 까지의 단어 갯수
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

count_list = [0] * 26

# 반복문을 돌면서 단어 세기
for i in range(len(word)):
    for j in range(len(alpha)):
        if word[i].upper() == alpha[j]:
            count_list[j] += 1

# max 값의 알파벳 찾기
max_count = max(count_list)
for i in range(len(count_list)):
    if count_list[i] == max_count:
        result = alpha[i]
    
# 값 같을때 예외처리하기
count = 0
for i in count_list:
    if max_count == i:
        count += 1
if count >= 2:
    result = '?'

print(result)