# 재귀

def binary_search(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    
    # 값을 찾으면 인덱스 반환
    if arr[mid] == target:
        return mid
    # 크다면 왼쪽 부분 재탐색
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    # 작다면 오른쪽 부분 재탐색
    else:
        return binary_search(arr, target, mid + 1, end)

target = 7
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search(array,target,0,len(array)-1)

if not result:
    print('존재하지 않습니다.')
else:
    print(result + 1)
    

#반복문 방법
def bi_se(arr, target, start, end):
    #시작이 끝보다 작을때만 while 문 실행
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        #중간점의 값이 타겟보다 크면 왼쪽 탐색 찾는 
        elif arr[mid] > target:
            end = mid - 1
        #중간점의 값이 타겟보다 작으면 오른쪽 탐색
        else:
            start = mid + 1
    return

target = 7
array = [1,3,5,7,9,11,13,15,17,19]

result = bi_se(array,target,0,len(array)-1)

if not result:
    print('존재하지 않습니다.')
else:
    print(result + 1)
        
        