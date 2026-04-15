
'''def zig_zag(nums):
    n = len(nums)

    for i in range(n):
        row = nums[i]

        if i % 2 != 0:
            row = row[::-1]

        
        for num in row:
            print(num,end=" ")'''



        # if i % 2 == 0:
        #     for j in range(0,len(nums[i])):
        #         print(nums[i][j],end=" ")

        # else:
        #     for j in range(len(nums[i])-1,-1,-1):
        #         print(nums[i][j],end=" ")

def matrix(nums):
    n = len(nums)

    for i in range(n):
        if i%2 ==0:
            for j in range(0,len(nums[i])):
                print(nums[i][j],end = " ")

        else:
            for j in range(len(nums[i])-1,-1,-1):
                print(nums[i][j],end = " ")


nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix(nums)


