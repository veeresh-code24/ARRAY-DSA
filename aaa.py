# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next


# def ConvertArray_LL(arr):
#     head = Node(arr[0])
#     movers = head
#     for i in range(1, len(arr)):
#         temp = Node(arr[i])
#         movers.next = temp
#         movers = temp

#     return head

# def MiddleLL(head):
#     cnt = 0
#     temp = head
#     while temp != None:
#         cnt += 1
#         temp = temp.next

    
#     res = (cnt//2)+1
#     temp = head
#     while temp != None:
#         res -= 1
#         if (res==0):
#             break
#         temp = temp.next

#     return temp.data


# def TraverseLL(head):
#     while head:
#         print(head.data,end=" ")
#         head = head.next

#     print()



# def main():
#     arr = [2,4,6,8,20]
#     head = ConvertArray_LL(arr)
#     TraverseLL(head)
#     length = MiddleLL(head)
#     print(length)

# if __name__ == '__main__':
#     main()

# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next


# def ConvertArray_LL(arr):
#     head = Node(arr[0])
#     movers = head
#     for i in range(1, len(arr)):
#         temp = Node(arr[i])
#         movers.next = temp
#         movers = temp

#     return head

# def  Reverse_LL(head):
#     if head == None or head.next == None:
#         return None
    
#     temp = head
#     stack = []

#     while temp != None:
#         stack.append(temp.data)
#         temp = temp.next

#     temp = head
#     while temp != None:
#         temp.data = stack.pop()
#         temp = temp.next

#     return head


# def TraverseLL(head):
#     while head:
#         print(head.data,end=" ")
#         head = head.next

#     print()



# def main():
#     arr = [2,4,6,8,20]
#     head = ConvertArray_LL(arr)
#     # TraverseLL(head)
#     length = Reverse_LL(head)
#     # print(length)
#     TraverseLL(head)

# if __name__ == '__main__':
#     main()

'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def ConvertArray_LL(arr):
    head = Node(arr[0])
    movers = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        movers.next = temp
        movers = temp

    return head

def  Reverse_LL(head):
    if head == None or head.next == None:
        return None
    
    temp = head
    prev = None

    while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front


    return prev
    


def TraverseLL(head):
    while head:
        print(head.data,end=" ")
        head = head.next

    print()



def main():
    arr = [2,4,6,8,20]
    head = ConvertArray_LL(arr)
    # TraverseLL(head)
    head = Reverse_LL(head)
    # print(length)
    TraverseLL(head)

if __name__ == '__main__':
    main()'''

# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next


# class Solution:
#     def CheckeLL_in_Loop(self,head):
#         if head == None or head.next == None:
#             return None
        
#         slow = head
#         fast = head

#         while fast != None and fast.next != None:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True
            
#         return False
            

# if __name__ == '__main__':
#     head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     fourth = Node(4)
#     fifth = Node(5)

#     head.next = second
#     second.next = third
#     third.next = fourth
#     fourth.next = fifth

#     # fifth.next = second
#     # third.next = second

# sol = Solution()
# startNode = sol.CheckeLL_in_Loop(head)

# if startNode:
#     print("Loop is present in linkedList")
# else:
#     print("Loop is not in linkedList")


'''class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class Solution:
    def CheckeLL_in_Loop(self,head):
        if head == None or head.next == None:
            return None
        
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self. CountLL(slow,fast)
            
        return 0
            

    def CountLL(self,slow,fast):

        fast = fast.next
        cnt = 1

        while slow != fast:
            cnt += 1
            fast = fast.next

        return cnt

        


        
        

if __name__ == '__main__':
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    fifth.next = second
    # third.next = second

sol = Solution()
startNode = sol.CheckeLL_in_Loop(head)

if startNode:
    print("Loop is present in linkedList",startNode)
else:
    print("Loop is not in linkedList")'''

# def largest_ele(nums):
#     nums.sort()

#     return nums[-1]

# nums = [10,2,1,200,2,3,100,3,4,5]
# print(largest_ele(nums))

# def largest_nums(nums):

#     largest = -1

#     for i in range(len(nums)):
#         if nums[i] > largest:
#             largest = nums[i]

#     return largest


# nums = [200,1,2,3,4,23,21]
# print(largest_nums(nums))

'''def second_largest(nums):
    nums.sort()
    first_lar = nums[-1]

    for i in range(len(nums)-1,-1):
        if nums[i] != first_lar:
            return nums[i]
        
nums = [2,46,21,12,45,3]
print(second_largest(nums))

def second_largest(nums):

    first_lar = second_lar = float('-inf')

    for i in range(len(nums)):
        if nums[i] > first_lar:
            first_lar = nums[i]


    for i in range(len(nums)):
        if nums[i] != first_lar and nums[i] > second_lar:
            second_lar = nums[i]

    return second_lar
        
nums = [101,21,34,1,2,4,53,100,200]
print(second_largest(nums))'''

'''def second_largest(nums):
    first_lar = second_lar = float('-inf')

    for i in range(len(nums)):
        if nums[i] > first_lar:
            second_lar = first_lar
            first_lar = nums[i]

        elif nums[i] != first_lar and nums[i] > second_lar:
            second_lar = nums[i]

    return second_lar


nums = [101,21,34,1,2,4,53,100,200,4000]
print(second_largest(nums))'''

'''def sorted_array(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] > nums[(i+1)%len(nums)]:
            count += 1
        
    return count <= 1


nums = [1,2,1,3]
print(sorted_array(nums))'''

# def sorted_arr(nums):
#     count = 0

#     for i in range(1,len(nums):
#         if nums[i] > nums[i+1]%len(nums):
#             count += 1

#     return count == 1




# nums = [3,4,5,1,2]
# print(sorted_arr(nums))

'''def remove_duplicate(nums):
    n = len(nums)

    st = set()
    for i in range(n):
        st.add(nums[i])

    index = 0
    for i in st:
        nums[index] = i
        index += 1

    return index

nums = [0 ,0, 3, 3,5, 6, 6]
print(remove_duplicate(nums))'''

# def remove_duplicate(nums):
#     n = len(nums)

#     i = 0
#     j = 1
#     while j < n:
#         if nums[j] != nums[i]:
#             nums[i+1] = nums[j]
#             j += 1
#             i += 1

#         else:
#             j += 1

        
#     return nums



# nums = [0 ,0, 3, 3,5, 6, 6]
# print(remove_duplicate(nums))

'''def fun():
    print(1)

    fun()

fun()'''

'''cnt = 0
def fun():
    global cnt
    if cnt > 10:
        return 
    print(cnt)
    cnt += 1

    fun()

fun()'''

# def fun(cnt):
#     if cnt > 10:
#         return 
    
#     print(cnt)
#     fun(cnt+1)

# fun(0)

# def fun(i,n):
#     if i > n:
#         return 
    
#     print("Iranna")
#     fun(i+1,n)

# fun(1,5)

'''def fun(i,n):
    if i > n:
        return 
    print(i)
    fun(i+1,n)

fun(1,10)
'''

# def fun(i,n):
#     if i < 1:
#         return 
    
#     print(i)
#     fun(i-1,n)

# fun(100,100)

'''def fun(i,n):
    if i < 1:
        return
    
    fun(i-1,n)
    print(i)

fun(5,5)'''

'''def fun(i,n):
    if i > n:
        return
    
    fun(i+1,n)
    print(i)

fun(1,5)'''

'''def fun(i,n):
    if i < 1:
        print(n)
        return 
    
    fun(i-1,n+i)

fun(6,0)'''

'''def fun(n):
    if n == 0:
        return 0
    
    return n + fun(n-1)

print(fun(3))'''


def fun(i,fact):
    if i <= 1:
        print(fact)
        return
    
    fun(i-1,fact*i)


fun(5,1)

'''def fun(n):
    if n == 0:
        return 1
    return n * fun(n-1)

print(fun(5))'''

    

    









