def aestroidCollision(aestroid):
    n = len(aestroid)
    st = []
    for i in range(n):
        if aestroid[i] > 0:
            st.append(aestroid[i])

        else:
            while st and st[-1] > 0 and st[-1] < abs(aestroid[i]):
                st.pop()


            if st and st[-1] == abs(aestroid[i]):
                st.pop()


            elif not st or st[-1] < 0:
                st.append(aestroid[i])

    return st


# aestroid = [3,5,-6,2,-1,4]
# aestroid = [8,-8]
# aestroid = [10,2,-5]
aestroid = [3,5,-6,2,-1,4]
print(aestroidCollision(aestroid))