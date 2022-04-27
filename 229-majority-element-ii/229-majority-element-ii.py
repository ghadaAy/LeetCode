class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        third = len(nums)/3
        nums.sort()
        i = 0
        r = []
        
        while i < len(nums):
            p = nums.count(nums[i])
            
            if p>third:
                r.append(nums[i])
            i += p
            
        return r
            