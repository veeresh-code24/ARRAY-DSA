def spiral_matrix(matrix):

    top = 0
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1
    res = []

    while top <= bottom and left <= right:
        for i in range(left,right+1):
            # print(matrix[top][i])
            res.append(matrix[top][i])

        top += 1

        for i in range(top,bottom+1):
            # print(matrix[i][right])
            res.append(matrix[i][right])
        right -= 1

        if(not(top <= bottom and left <= right)):
            break

        for i in range(right,left-1,-1):
            # print(matrix[bottom][i])
            res.append(matrix[bottom][i])
        bottom -=  1

        for i in range(bottom,top-1,-1):
            # print(matrix[i][left])
            res.append(matrix[i][left])
        left += 1

        return res

matrix = [[1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16],
[17,18,19,20,21,22,23,24],
[25,26,27,28,29,30,31,32],
[33,34,35,36,37,38,39,40],
[41,42,43,44,45,46,47,48]]

print(spiral_matrix(matrix))
