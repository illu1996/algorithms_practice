# pg 42577
# 전화번호 목록

def solution(pb):

    answer = True
    pb.sort()
    for i in range(len(pb)-1):
        if pb[i] in pb[i+1][:len(pb[i])]:
            answer =False
            break
    return answer