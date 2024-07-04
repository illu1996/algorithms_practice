# pg 12906
# 같은 숫자는 싫어
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        # 마지막 값이 i 면 패스
        if answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer


# 다른 풀이
def solution(arr):
    # 함수를 완성하세요
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a