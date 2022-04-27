class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        nums.append(-1)
        r_list = []
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == target:
                if len(r_list)==0:
                    r_list.append(i)
                    count += 1
                else:
                    count += 1
            elif count != 0:
                r_list.append(i-1)
                break
                
        if len(r_list)==0 :
            return [-1,-1]
        
        if len(r_list)==1 :
            return [r_list[0],r_list[0]]
        
        return r_list