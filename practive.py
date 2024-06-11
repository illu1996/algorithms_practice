def binary_search(arr, s, e, k):
    if s > e:
        return
    mid = (s+e)// 2
    
    if arr[mid] == k:
        return mid
    if arr[mid] > k:
        return binary_search(arr,s,mid-1,k)
    else:
        return binary_search(arr,mid+1,e,k)
    
def bi_se(arr,s,e,k):
    
    while s<=e:
        mid = (s+e) // 2
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            e = mid -1
        else:
            s = mid + 1
    return None
        