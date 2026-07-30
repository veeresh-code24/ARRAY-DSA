def subset_string(s,ans):
    if len(s) == 0:
        print(ans)
        return
    
    # pick
    subset_string(s[1:],ans+s[0])

    # NOT pick
    subset_string(s[1:],ans)

def main():
    s = input()
    subset_string(s,'')

if __name__ == "__main__":
    main()
