from collections import deque

class myQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que =myQueue()
        result = []
        for i in range(k):
            que.push(nums[i])

        result.append(que.front())

        for i in range(k, len(nums)):
            que.pop(nums[i - k])
            que.push(nums[i])
            result.append(que.front())
        
        return result