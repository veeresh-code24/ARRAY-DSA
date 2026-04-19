# Brute Force

'''def valid_anagram(s,t):

    if len(s) != len(t):
        return False
    
    if sorted(s) == sorted(t):
        return True
    
    return False
# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"

print(valid_anagram(s,t))'''

# Optimization

def valid_anagram(s,t):

    if len(s) != len(t):
        return False
    s = s.upper()
    t = t.upper()
    
    freq = [0] * 26

    for char in s:
        freq[ord(char) - ord("A")] += 1

    for char in t:
        freq[ord(char) - ord("A")] -= 1


    for count in freq:
        if count != 0:
            return False
        
    return True

# s = "anagram"
# t = "nagaram"
s = "rat"
t = "car"
print(valid_anagram(s,t))

    

