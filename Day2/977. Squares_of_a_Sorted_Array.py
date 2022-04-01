class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        res=[]
        if j==0:
            res.append(nums[j]*nums[j])
            return res
        while i<=j:
            if -(nums[i])>nums[j]:
                res.append(nums[i]*nums[i])
                i+=1
            else:
                res.append(nums[j]*nums[j])
                j-=1
            
        return res[::-1]