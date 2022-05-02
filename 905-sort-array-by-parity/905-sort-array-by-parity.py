class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        result = list()
        n = len(nums)
        
        for i in range(n):
            if nums[i]%2 == 0:
                result.insert(0,nums[i])
            else:
                result.insert(n-1,nums[i])
                
        return result
            