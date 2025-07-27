class Solution:
    def getnum(self, num:int) -> int:
        sum = 0
        new_num = str(num)
        for i in new_num:
            i = int(i)
            sum += i * i
        return sum

    def isHappy(self, n: int) -> bool:
        sum = []
        while True:
            new_sum = self.getnum(n)
            sum.append(new_sum)
            n = new_sum
            if n in sum:
                return False
            if n == 1:
                return True
        
sol = Solution()
print(sol.isHappy(19))