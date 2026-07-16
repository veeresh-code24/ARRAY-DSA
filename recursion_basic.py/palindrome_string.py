def fun(i,string,n):
    if i >= n//2:
        return True
    
    if string[i] != string[n-i-1]:
        return False
    
    return fun(i+1,string,n)

def main():
    string = "MADSM"
    n = len(string)
    print(fun(0,string,n))

main()
