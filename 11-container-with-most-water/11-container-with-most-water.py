class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        max_h = 0
        i = 0
        j = l-1
        while(i<j):
            leng = min(height[i],height[j])
            area = leng*(abs(j-i))
            max_h = max(area, max_h)
            
            if height[i]>=height[j]:
                  j -= 1
            else:
                i += 1
        return max_h