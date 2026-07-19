
def power_of(x,y):
    if y == 0:
        return 1
    
    return power_of(x,y-1)*x

def main():
    print(power_of(5,8))

main()

# Little Bit Efficient

def power_of(x,y):
    if y == 0:
        return 1
    
    if y % 2 == 0:
        return  power_of(x,y//2) * power_of(x,y//2)
    
    else:
        return power_of(x,y-1) * x
    
def main():
    print(power_of(5,8))

main()


# More Efficient

def power_of(x,y):
    if y == 0:
        return 1
    
    if y % 2 == 0:
        res = power_of(x,y//2)
        return res* res
    
    else:
        return power_of(x,y-1) * x
    
def main():
    print(power_of(5,4))

main()