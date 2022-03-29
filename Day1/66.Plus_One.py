class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for j in range(len(digits)):
            digits[j]=str(digits[j])
        a=''.join(digits)
        d=int(a,10)
        d+=1
        array=str(d)
        res=[]
        for i in array:
            res.append(int(i,10))
        return res