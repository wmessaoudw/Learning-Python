def binary_search(lis,target):
    left=0
    right=len(lis)-1
    while left<=right:
           mid=left+(right-left)//2
           if lis[mid]==target:
               return mid
           elif lis[mid]<target:
               left=mid+1 #it's in right side
           else:
               right=mid-1 #it's in left side
    return -1
lis=[1,2,3,4,5,7,9]
print(binary_search(lis,3))