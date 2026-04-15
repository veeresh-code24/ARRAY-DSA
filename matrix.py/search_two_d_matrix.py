def tw_d(nums,target):


    column = len(nums[0])
    for i in range(len(nums)):

        for j in range(column):
            if nums[i][j] == target:
                return True
            

    return False


nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 15

print(tw_d(nums,target))