from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        sum = 0
        left = 0
        for right in range(len(nums)):
            sum += nums[right]
            while(sum >= target):
                sum -= nums[left] 
                length = right - left + 1
                result = min(result,length)
                left += 1
        return result


            

# 示例测试
solution = Solution()
target = 7
nums = [2,3,1,2,4,3]
result = solution.minSubArrayLen(target, nums)
print(result)  # 预期输出：2
