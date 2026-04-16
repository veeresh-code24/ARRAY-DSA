'''def reverse_string(s):
    words = s.split()
    n = words[::-1]
    m = " ".join(n)
    return m



s = " the sky    is blue "
print(reverse_string(s))'''

# Brute force

def reverse_word(s):

    li = []
    word = ""

    for char in s:
        if char != " ":
            word += char

        elif word:
            li.append(word)
            word = ""


    if word:
        li.append(word)

    li.reverse()

    return " ".join(li)


# s = "Nowdays i am becoming lazy"
# s = "  hello world  "
s = "a good   example"
print(reverse_word(s))