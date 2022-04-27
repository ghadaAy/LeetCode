class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
            smallest_diff = 10000000
            smallest_diff_i = 10000000
            if target<nums[0]:
                return 0
            elif target>nums[len(nums)-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    if smallest_diff>target-nums[i] and target-nums[i]>=0:
                        smallest_diff = target-nums[i]
                        smallest_diff_i = i
                if smallest_diff == 0:
                    return smallest_diff_i
                else:
                    return smallest_diff_i+1