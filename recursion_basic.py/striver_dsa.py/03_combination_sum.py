def findCombination(ind, arr, target, ans, ds):

    # Base case
    if ind == len(arr):
        if target == 0:
            ans.append(list(ds))
        return

    # TAKE
    if arr[ind] <= target:

        ds.append(arr[ind])

        findCombination(
            ind,
            arr,
            target - arr[ind],
            ans,
            ds
        )

        # Undo / backtrack
        ds.pop()

    # NOT TAKE
    findCombination(
        ind + 1,
        arr,
        target,
        ans,
        ds
    )


def combinationSum(candidate, target):

    ans = []
    ds = []

    findCombination(0, candidate, target, ans, ds)

    return ans


candidate = [2, 3, 6, 7]
target = 8

print(combinationSum(candidate, target))