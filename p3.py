import math

class Solution:
    def Log2(self,x):
        return (math.log10(x) /
                math.log10(2))

    def isPowOfTwo(self,n):
        return (math.ceil(self.Log2(n)) == math.floor(self.Log2(n)))
    
    def countPairs(self, deliciousness: List[int]) -> int:

        sum = 0
        for i in range(0, len(deliciousness) - 1):
            for j in range(i, len(deliciousness) - 1):
                if ( self.isPowOfTwo(deliciousness[i] + deliciousness[j]) ):
                    sum += 1
        return sum