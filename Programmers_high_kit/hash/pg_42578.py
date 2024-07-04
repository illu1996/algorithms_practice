# pg 42578
# 의상

def solution(clothes):
    ans = 1
    dic = {}
    
    # 옷 담기
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = [i[0]]
        else:
            dic[i[1]].append(i[0])

    # n개와 m개의 모든 경우의 수는 n*m
    
    
    length = []
    # 각 종류별 개수 구하기
    for i in dic:
        length.append(len(dic[i]))
    
    for i in length:
        # 옷을 안입는 경우도 포함하여 i+1을 곱함
        ans *= i+1
    # 모두 안입는 경우 제거
    ans -= 1

    return ans