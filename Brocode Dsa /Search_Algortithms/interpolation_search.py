def interpolation_search(lis,target):
    high=len(lis)-1
    low=0
    while low<=high and lis[low]<=target<=lis[high]:
        if lis[low]==lis[high]:
            return low if lis[low]==target else  -1
        probe=low + (high-low) * (target-lis[low])//(lis[high]-lis[low])
        if target==lis[probe]:
            return probe
        elif target<lis[probe]:
            high=probe-1
        else:
            low=probe+1
    return -1
