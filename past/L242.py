class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        index = [0]* 26
        for word in s:
            index[ord(word) - ord("a")] += 1
        for word in t:
            index[ord(word) - ord("a")] -= 1
        if index == [0]*26:
            return True
        else:
            return False

sol = Solution()
print(sol.isAnagram("anagram","nagaram"))