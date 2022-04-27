class Solution:
    def reverse(self, x: int) -> int:
        
        if x>=0:
            xx = str(x)
            r = xx[::-1]
            rr = int(r)
            if rr>-2147483648 and rr< 2147483647:
                return int(r)
            else: return 0
        else:
            xx = str(x)
            r = xx[::-1]
            rr = -1*int(r[:len(r)-1])
            if rr>-2147483648 and rr< 2147483647:
                return(rr)
            else: return 0
                
      
                