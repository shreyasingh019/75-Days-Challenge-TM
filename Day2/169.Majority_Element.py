class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        if n==1:
            return nums[0]
        
        for i in nums:
            d[i]=d.get(i,0)+1
            
        for j in d.keys():
            if d[j]>(n//2):
                return j