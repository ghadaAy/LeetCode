class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        max_h = 0
        i = 0
        j = l-1
        while(i<j):
            
            leng = min(height[i],height[j])
            area = leng*(abs(j-i))
            if max_h<area:
                max_h = area
            if height[i]>=height[j]:
                  j -= 1
            else:
                i += 1
        return max_h