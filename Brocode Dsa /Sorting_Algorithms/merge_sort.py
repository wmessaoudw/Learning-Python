def merge_sort(lis):
    if len(lis)<=1:
        return lis
    middle=len(lis)//2
    left_lis=merge_sort(lis[:middle])
    right_lis=merge_sort(lis[middle:])
    return merge(left_lis,right_lis)
def merge(left_lis,right_lis):
    res=[]
    i=j=0
    while i<len(left_lis) and j<len(right_lis):
        if left_lis[i] <= right_lis[j]:
            res.append(left_lis[i])
            i+=1
        else:
            res.append(right_lis[j])
            j=j+1
    res.extend(left_lis[i:])
    res.extend(right_lis[j:])
    return res
lis=[2,3,4,1,2,3,56,1,2,4,6,1,41,4,1,0]
res=merge_sort(lis)
print(res)
