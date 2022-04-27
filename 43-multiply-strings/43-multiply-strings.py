class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        s1,s2 = 0,0
        if len(num1)==1 and len(num2)==1:
            return str(int(num1)*int(num2))
        else:
            k1 = len(num1)
            k2 = len(num2)

            for i in range(0,k1):
                s1 += int(num1[i])*10**(k1-1-i)
            for i in range(0,k2):
                s2 += int(num2[i])*10**(k2-1-i)
            return str(s1*s2)