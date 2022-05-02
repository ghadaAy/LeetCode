class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        result = list()
    
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                result.insert(0,nums[i])
            else:
                result.append(nums[i])
                
        return result
            