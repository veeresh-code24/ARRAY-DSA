# Brute force

def merge_interval(intervals):
    n = len(intervals)
    intervals.sort()
    arr = []

    i = 0

    while i < n:
        start  = intervals[i][0]
        end = intervals[i][1]

        j = i+1
        while j < n and intervals[j][0] <= end:
            end = max(end, intervals[j][1])
            j += 1

        arr.append([start,end])

        i = j

    return arr
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_interval(intervals))