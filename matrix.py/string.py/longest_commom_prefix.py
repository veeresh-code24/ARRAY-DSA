
# Better
def longest_common_pre(strs):
    n = len(strs)

    if not strs:
        return ""
    
    first = strs[0]
    last = strs[-1]
    ans = []

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return "".join(ans)
        
        ans.append(first[i])

    return "".join(ans)

# strs = ["flower","flow","flight"]
strs = ["iranna","irannask","irannakanamadi"]
# strs = ["dog","racecar","car"]
print(longest_common_pre(strs))

# Optimal

'''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]

        i = 0
        while i < min(len(first), len(last)) and first[i] == last[i]:
            i += 1

        return first[:i]'''


