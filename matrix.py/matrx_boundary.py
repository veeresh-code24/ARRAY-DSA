def matrix_boundary(nums):

    i,j = 0,0

    for j in range(0,len(nums)):
        print(nums[i][j],end=" ")

    j = len(nums)-1
    for i in range(1,len(nums)):
        print(nums[i][j],end=" ")

    i = len(nums)-1

    for j in range(len(nums)-2,-1,-1):
        print(nums[i][j],end=" ")

    j = 0
    for i in range(len(nums)-2,0,-1):
        print(nums[i][j],end=" ")

nums = [[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]]

matrix_boundary(nums)

'''def matrix_boundary(nums):

    rows = len(nums)
    cols = len(nums[0])

    # 1. Top row
    for j in range(cols):
        print(nums[0][j])

    # 2. Right column
    for i in range(1, rows):
        print(nums[i][cols - 1])

    # 3. Bottom row
    for j in range(cols - 2, -1, -1):
        print(nums[rows - 1][j])

    # 4. Left column
    for i in range(rows - 2, 0, -1):
        print(nums[i][0])'''
