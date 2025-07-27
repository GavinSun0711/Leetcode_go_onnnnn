class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def getRightBorder(nums: list[int], target:int) -> int:
            left = 0
            right = len(nums) - 1
            rightBorder = -2
            while(left <= right):
                middle = (left + right) // 2
                if(nums[middle] > target):
                    right = middle -1
                else:
                    left = middle + 1
                    rightBorder = left
            return rightBorder

        def getLeftBorder(nums:list[int], target:int) -> int:
            left = 0
            right = len(nums) - 1
            leftBorder = -2
            while(left <= right):
                middle = (left + right) // 2
                if(nums[middle] >= target):
                    right = middle - 1
                    leftBorder = right
                else:
                    left = middle + 1
            return leftBorder

        leftBorder = getLeftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)

        if(leftBorder == -2 or rightBorder == -2):
            return[-1. -1]
        elif(rightBorder - leftBorder > 1):
            return[leftBorder + 1, rightBorder - 1]
        else:
            return[-1, -1]

solution = Solution()

# 定义测试数据
nums = [5, 7, 7, 8, 8, 10]
target = 6

# 调用searchRange方法并打印结果
result = solution.searchRange(nums, target)
print(result)  # 输出 [-1, -1]