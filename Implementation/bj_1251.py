# 백준 1251 단어나누기
# 실버5 
from itertools import product

n = list(input())
# 단어의 길이
length = len(n)

# 전체길이로 자르는 중복 조합  만들기
rangeN = list(range(1,length+1))

n_lst = list(product(rangeN,repeat=3))
cor_lst = list(filter(lambda x:sum(x) == length,n_lst)) 

# 모든 단어 리스트
word = []

# COR_LST 길이만큼 단어 자르고 붙이기
for i in range(len(cor_lst)):
    a,b,c = cor_lst[i]
    first_word = n[0:a]
    second_word = n[a:a+b]
    third_word = n[a+b:]
    
    # 단어 뒤집기
    reverse_word = list(reversed(first_word)) + list(reversed(second_word))+list(reversed(third_word))
    word.append(''.join(reverse_word))

# 정렬하기
word.sort()

print(word[0])

