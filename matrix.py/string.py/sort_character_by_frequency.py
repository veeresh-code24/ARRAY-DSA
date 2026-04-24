
'''"Time complexity is O(n + k log k) where k is number of unique characters.
In worst case it's O(n log n), but usually it's closer to O(n)."

def sort_character(s):

    freq = {}

    for char in s:
        freq[char] = freq.get(char,0)+1

        sor_fre = sorted(freq.items(),key=lambda x :-x[1] )

        res = []
        for ch,count in sor_fre:
            res.append(ch*count)

    return "".join(res)

We can optimize sorting using bucket sort and make it strictly O(n)

s = "tree"
# s = "cccaaa"
# s = "Aabb"
print(sort_character(s))'''


def sort_character(s):
    freq = {}

    for char in s:
        freq[char] = freq.get(char,0) + 1

    sort_fre = sorted(freq.items(), key=lambda x : -x[1])

    res = []

    for ch,count in sort_fre:
        res.append(ch*count)

    return "".join(res)


# s = "tree"
# s = "cccaaa"
s = "Aabb"
print(sort_character(s))