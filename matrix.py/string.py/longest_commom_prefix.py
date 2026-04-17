def longest_common_pre(strs):
    n = len(strs)

    for i in range(n):
        res = []
        for j in range(n):
            if strs[j] == strs[i]:
        
        
                res.append(strs[i])


    return res


strs = ["flower","flow","flight"]
print(longest_common_pre(strs))