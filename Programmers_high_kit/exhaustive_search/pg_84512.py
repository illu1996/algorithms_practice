# pg 84512
# 모음사전
# 레벨 2

from itertools import product

def solution(word):
    answer = 0
    # 모음 종류
    lst = ['A','E','I','O','U']
    dic = []
    # 만들수 있는 모든 단어
    for i in range(1,len(lst)+1):
        # 중복 순열
        comb = list(product(lst,repeat=i))
        for j in comb:
            dic.append(''.join(j))
    dic.sort()

    return dic.index(word)+ 1