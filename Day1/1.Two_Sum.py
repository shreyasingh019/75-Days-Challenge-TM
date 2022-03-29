class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(nums)):
            temp=target-nums[i]
            if (temp in nums) and i!=nums.index(temp):
                res.append(i)
                res.append(nums.index(temp))
                return res
                