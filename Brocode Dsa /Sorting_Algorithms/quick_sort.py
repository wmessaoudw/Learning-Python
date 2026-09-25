def quick_sort(lis):
    if len(lis)<=1:
        return lis
    pivot=lis[len(lis)//2]
    left=[x for x in lis if x<pivot]
    middle=[x for x in lis if x==pivot]
    right=[x for x in lis if x>pivot]
    return quick_sort(left) + middle +quick_sort(right)

