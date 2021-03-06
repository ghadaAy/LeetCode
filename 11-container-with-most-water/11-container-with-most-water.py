class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_h = 0
        i = 0
        j = len(height)-1
        for _ in range(i, j):
            leng = min(height[i],height[j])
            area = leng*(abs(j-i))
            max_h = max(area, max_h)
            
            if height[i]>=height[j]:
                  j -= 1
            else:
                i += 1
                
            if j <= i:
                break
        return max_h