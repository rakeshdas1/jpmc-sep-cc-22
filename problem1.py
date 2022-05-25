class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = 0
        for i in range(len(deliciousness)):
            for j in range(i+1, len(deliciousness)):
                d = deliciousness[i] + deliciousness[j]
                while d % 2 == 0:
                    d //= 2
                if d == 1:
                    count += 1 
        return count % (10 ** 9 + 7)