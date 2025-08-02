class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result_list = []
        for item in tokens:
            if item == "+" or item == "-" or item == "*" or item == "/":
                if item == "+":
                    new = int(result_list[-2]) + int(result_list[-1])
                    result_list.pop()
                    result_list.pop()
                    result_list.append(new)
                elif item == "-":
                    new = int(result_list[-2]) - int(result_list[-1])
                    result_list.pop()
                    result_list.pop()
                    result_list.append(new)
                elif item == "*":
                    new = int(result_list[-2]) * int(result_list[-1])
                    result_list.pop()
                    result_list.pop()
                    result_list.append(new)
                elif item == "/":
                    new = int(result_list[-2]) / int(result_list[-1])
                    result_list.pop()
                    result_list.pop()
                    result_list.append(int(new))
            else:
                result_list.append(item)
        return int(result_list[-1])