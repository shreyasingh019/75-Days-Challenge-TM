class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return -1
        pre=[0]*n
        pre[0]=nums[0]
        post=[0]*n
        post[n-1]=nums[-1]
        for i in range(1,n):
            pre[i]=pre[i-1]+nums[i]
        
        for j in range(n-2,-1,-1):
            post[j]=post[j+1]+nums[j]

        for k in range(n):
            if pre[k]==post[k]:
                return k