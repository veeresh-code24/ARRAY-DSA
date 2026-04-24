# Brute Force

'''def fruit_into_basket(fruits):
    n = len(fruits)
    max_len = 0


    for i in range(n):
        st = set()
        for j in range(i,n):
            st.add(fruits[j])

            if len(st) > 2:
                break

            max_len = max(max_len,j-i+1)

    return max_len
# fruits = [1, 2, 3, 2, 2]
fruits = [1, 2, 1]

print(fruit_into_basket(fruits))'''

# Brute Better

'''def fruit_into_basket(fruits):
    n = len(fruits)
    max_len = 0

    for start in range(n):
        basket = {}
        for end in range(start,n):
            basket[fruits[end]] = basket.get(fruits[end],0)+1

            if len(basket) > 2:
                break

            max_len = max(max_len,end-start+1)

    return max_len


# fruits = [1, 2, 3, 2, 2]
fruits = [1, 2, 1]

print(fruit_into_basket(fruits))'''

# Optimizations

def fruit_into_basket(fruits):
    n = len(fruits)
    max_len = 0
    left = 0
    basket = {}

    for right in range(n):
        basket[fruits[right]] = basket.get(fruits[right],0)+1

        while len(basket) > 2:
            basket[fruits[left]] -= 1

            if basket[fruits[left]] == 0:
                del basket[fruits[left]]

            left += 1

        max_len = max(max_len,right-left+1)

    return max_len




fruits = [1, 2, 3, 2, 2]
# fruits = [1, 2, 1]

print(fruit_into_basket(fruits))















