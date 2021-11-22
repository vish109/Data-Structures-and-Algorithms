
def search(nums,target):
    l=0
    r=len(nums)-1
    while(l<=r):
        m=l+(r-l)//2
        if(nums[m]<target):
            l=m+1
        elif(nums[m]>target):
            r=m-1
        else:
            return m
    return -1

def recursive_search(nums,target,l,r):
    m=l+(r-l)//2
    if(l<=r):
        if(nums[m]>target):
            return recursive_search(nums,target,l,m-1)
        elif(nums[m]<target):
            return recursive_search(nums,target,m+1,r)
        else:
            return m
    return -1
nums=[1,2,3,5,6,8,9]
target=4
print(search(nums,target))
print(recursive_search(nums,target,0,len(nums)-1))