# Brute
'''def tw_d(nums,target):


    column = len(nums[0])
    for i in range(len(nums)):

        for j in range(column):
            if nums[i][j] == target:
                return True
            

    return False


nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 15

print(tw_d(nums,target))'''


# Better


'''def tw_d(matrix,target):

    i = 0
    j = len(matrix[0])-1

    while i < len(matrix) and j >= 0:
        if target == matrix[i][j]:
            return True
        
        elif target < matrix[i][j]:
            j -= 1

        else:
            i += 1

    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 100

print(tw_d(matrix,target))'''



def tw_d(matrix,target):
    n = len(matrix)
    m = len(matrix[0])

    left = 0
    right = n * m-1

    while left <= right:
        mid = (left+right)//2
        row = mid//m
        col = mid%m

        if matrix[row][col] == target:
            return True
        
        elif matrix[row][col] < target:
            left = mid +1

        else:
            right = mid-1


    return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 21

print(tw_d(matrix,target))



