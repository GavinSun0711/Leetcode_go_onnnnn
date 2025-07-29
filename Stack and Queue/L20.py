class Solution:
    def isValid(self, s: str) -> bool:

        ans_stack = []

        for item in s:
            #这样反着放方便比较
            if item == "(":
                ans_stack.append(")")
            elif item == "{":
                ans_stack.append("}")
            elif item == "[":
                ans_stack.append("]") 
            # 先判断这个 否则会空用
            # 如果已经空 错
            elif not ans_stack:
                return False
            # 如果匹配， pop
            elif item == ans_stack[-1]:
                ans_stack.pop()
            #如果不匹配 则直接报错
            elif item != ans_stack[-1]:
                return False


        #如果最后还剩下 错
        if ans_stack:
            return False
        
        return True
#还有一种 是进一个匹配一个 但是双重if 会更多内存消耗
class Solution:
    def isValid(self, s: str) -> bool:
        ans_stack = []
        for item in s:
            if ans_stack:
                if ans_stack[-1] == "(" and item == ")":
                    ans_stack.pop()
                elif ans_stack[-1] == "[" and item == "]":
                    ans_stack.pop()
                elif ans_stack[-1] == "{" and item == "}":
                    ans_stack.pop()
                else:
                    ans_stack.append(item)
            else:
                ans_stack.append(item)
        
        if ans_stack:
            return False
        
        return True