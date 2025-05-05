# 퀵 정렬
# pivot 정렬

lst = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(lst,s,e):
    
    if s >= e:
        return
    p = s
    l = s + 1
    r = e
    
    while (l <= r):
        while l <= e and lst[l] <= lst[p]:
            l += 1
        while (r > s and lst[r] >= lst[p]):
            r -= 1
        
        if l > r:
            lst[r],lst[p] =lst[p],lst[r]
        else:
            lst[l],lst[r] =lst[r],lst[l]
    quick_sort(lst,s,r-1)
    quick_sort(lst,r+1,e)

quick_sort(lst,0,len(lst)-1)
print(lst)