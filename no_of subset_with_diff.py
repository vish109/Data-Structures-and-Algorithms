
def count(nums,diff):
    n=len(nums)
    s=sum(nums)
    s1=(diff+s)//2
    dp=[[0 for i in range(s1+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,s1+1):
            if(nums[i-1]<=j):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][s1]

nums=[1,1,2,3]
diff=1
print(count(nums,diff))