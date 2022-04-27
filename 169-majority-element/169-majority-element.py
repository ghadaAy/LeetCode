class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half = len(nums)/2
        
        nums.sort()
        
        for i in range(int(half*2)):
            if nums[i] != nums[i-1] or i==0:
                if nums.count(nums[i])>half:
                    return nums[i]
        