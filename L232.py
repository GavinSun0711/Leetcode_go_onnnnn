class MyQueue:

#注意self的用法，self是这个类的对象本身的东西，如果没有，则不知道是哪个。
#self也可以带上函数，意思是本类的对象所带的函数。
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        #这里调用的是下面自己写的empty，而不是本身所有的
        if self.empty():
            return None
        
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        result = self.pop()
        self.stack_out.append(result)
        return result

    def empty(self) -> bool:
        #这里为什么不能用empty？ 
        #因为这里的empty是自己写的
        if self.stack_in or self.stack_out:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()