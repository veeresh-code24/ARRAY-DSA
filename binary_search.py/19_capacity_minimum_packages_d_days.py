# Brute Force

# Normal function outside class
'''def daysNeeded(weights, capacity):
    days = 1
    currentLoad = 0

    for w in weights:
        if currentLoad + w > capacity:
            days += 1
            currentLoad = w
        else:
            currentLoad += w

    return days


class Solution:

    def shipWithinDays(self, weights, d):

        left = max(weights)
        right = sum(weights)

        for capacity in range(left, right + 1):

            needed = daysNeeded(weights, capacity)

            if needed <= d:
                return capacity

        return right


weights = [5,4,5,2,3,4,5,6]
d = 5

sol = Solution()

print(sol.shipWithinDays(weights, d))'''

# Time Complexity: O((sum_weights - max_weight) * N)

'''def capa_ship_packages(weights,capacity):

    days = 1
    currentload = 0

    for w in weights:
        if currentload + w > capacity:
            days += 1
            currentload = w
        else:
            currentload += w

    return days

def shipwithindays(weights,d):

    left = max(weights)
    right = sum(weights)

    for capacity in range(left,right+1):

        possible = capa_ship_packages(weights,capacity)

        if possible <= d:
            return capacity
        
    return right


weights = [1,2,3,4,5,6,7,8,9,10]
d = 5
print(shipwithindays(weights,d))

# Time Complexity: O((sum_weights - max_weight) * N)'''


# Optimization

class Solution:
    # Function to calculate how many days are needed to ship
    # all packages with the given ship capacity
    def daysNeeded(self, weights, capacity):
        # Initialize count of days to 1
        days = 1
        # Initialize current load on ship to 0
        currentLoad = 0

        # Iterate over all package weights
        for w in weights:
            # Check if adding current package exceeds capacity
            if currentLoad + w > capacity:
                # If yes, increase days count since we start a new day
                days += 1
                # Reset current load to current package weight
                currentLoad = w
            else:
                # Else, add current package weight to current load
                currentLoad += w
        # Return total days required
        return days

    # Function to find minimum ship capacity to ship all packages within d days
    def shipWithinDays(self, weights, d):
        # Calculate minimum capacity as max weight in packages
        left = max(weights)
        # Calculate maximum capacity as sum of all weights
        right = sum(weights)

        # Binary search between left and right capacity values
        while left < right:
            # Calculate mid value to test
            mid = left + (right - left) // 2
            # Calculate how many days needed for capacity mid
            needed = self.daysNeeded(weights, mid)

            # If days needed is less or equal to allowed days,
            # try to find smaller capacity on left side
            if needed <= d:
                right = mid
            else:
                # Else, need more capacity, search on right side
                left = mid + 1

        # Return minimum capacity found
        return left


if __name__ == "__main__":
    # Define array of package weights
    weights = [5,4,5,2,3,4,5,6]
    # Define number of days allowed for shipping
    d = 5
    # Create Solution object
    sol = Solution()
    # Print minimum capacity required to ship within d days
    print(sol.shipWithinDays(weights, d))
