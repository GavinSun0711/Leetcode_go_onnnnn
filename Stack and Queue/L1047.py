class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for item in s:
            if ans and item == ans[-1]:
                ans.pop()
            else:
                ans.append(item)
        #'分隔符'.join(可迭代对象)
        return "".join(ans)