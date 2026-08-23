def largestRectangleArea(heights):
    n = len(heights)
    stack = []
    leftsmall = [0] * n
    rightsmall = [0] * n

    # Nearest Smaller Element

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if not stack:
            leftsmall[i] = 0

        else:
            leftsmall[i] = stack[-1] + 1

        stack.append(i)

    stack.clear()

    # rightsmall 
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if not stack:
            rightsmall[i] = n-1
        else:
            rightsmall[i] = stack[-1] - 1

        stack.append(i)

    max_area = 0

    for i in range(n):
        width = rightsmall[i] - leftsmall[i] + 1
        max_area = max(max_area, heights[i] * width)

    return max_area

heights = [2, 1, 5, 6, 2, 3, 1]
print(largestRectangleArea(heights))


