# deque 是 Python collections 模块里的一个类，全称是 Double-Ended Queue（双端队列）。

# 与普通列表 (list) 不同，deque 在两端添加和删除元素的效率非常高（时间复杂度 O(1)）。



from collections import deque

# 初始化
q = deque()

# 尾部添加
q.append(1)       # -> [1]
q.append(2)       # -> [1, 2]

# 头部添加
q.appendleft(0)   # -> [0, 1, 2]

# 尾部弹出
x = q.pop()       # -> 2, 剩下 [0, 1]

# 头部弹出
y = q.popleft()   # -> 0, 剩下 [1]


class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

        return self.que.popleft()
        

    def top(self) -> int:
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        ans = self.que.popleft()
        self.que.append(ans)
        return ans

    #学习一下这个非
    def empty(self) -> bool:
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()