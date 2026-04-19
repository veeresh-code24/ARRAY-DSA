def rotate_string(s,goal):

    if len(s) != len(goal):
        return False
    
    s = s + s
    if goal in s:
        return True
    return False


# s = "abcde"
# goal = "cdeab" 
s = "abcde"
goal = "abced"

print(rotate_string(s,goal))