class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
        
        return res


sol = Solution()
sol.intersection([1,2,2,1],[2,2])
