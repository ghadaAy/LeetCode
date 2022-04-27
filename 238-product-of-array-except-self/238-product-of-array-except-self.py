class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if nums ==  [0] * len(nums):
            return [0] * len(nums)
        
        flag = False
        prod = 1
        nb=0
        
        for x in nums:
            if x!=0 or (x==0 and nb>0):
                print(x,nb)
                prod = prod * x
            else: 
                print(x,nb)
                flag = True
                nb += 1
        
        if not flag :
            return [int(prod*(num**(-1))) for num in nums]
        else:
            return [int(prod) if num == 0 else 0 for num in nums]