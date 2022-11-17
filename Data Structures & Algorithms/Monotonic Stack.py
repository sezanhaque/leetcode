"""
Discussion Link:
https://leetcode.com/tag/monotonic-stack/discuss/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems

What is monotonic stack?
There could be four types of monotonic stacks. Please read them carefully, 
we'll refer to these types at multiple places in the sections below.

1.  Strictly increasing - every element of the stack is strictly greater than the previous element. 
    Example - [1, 4, 5, 8, 9]

2.  Increasing - every element of the stack is greater than or equal to the previous element. 
    Example - [1, 4, 5, 5, 8, 9, 9]

3.  Strictly decreasing - every element of the stack is strictly smaller than the previous element.
    Example - [9, 8, 5, 4, 1]

4.  Decreasing - every element of the stack is smaller than or equal to the previous element. 
    Example - [9, 9, 8, 5, 5, 4, 1]

Finding next greater and previous greater elements require building a monotone decreasing stack (3 or 4). 
For finding next smaller and previous smaller requires building a monotone increasing stack (1 or 2). 
To help you remember this, think of this as an inverse relation - 
    *   Greater requires decreasing stacks, 
    *   Smaller requires increasing stacks.

*** If you have to find in the same list then use index of the list.
*** If you have to find from other list then use dictionary to track values.


markdown table:

|  Problem           |  Stack Type                  |  Operator in while loop |  Assignment Position  |
|--------------------|------------------------------|-------------------------|-----------------------|
|  next greater      |  decreasing (equal allowed)  |  stackTop < current     |  inside while loop    |
|  previous greater  |  decreasing (strict)         |  stackTop <= current    |  outside while loop   |
|  next smaller      |  increasing (equal allowed)  |  stackTop > current     |  inside while loop    |
|  previous smaller  |  increasing (strict)         |  stackTop >= current    |  outside while loop   |

"""

from collections import deque
from math import inf


def findNextGreater(nums: list[int]) -> list[int]:
    """
    4.  Decreasing - every element of the stack is smaller than or equal to the previous element.

    *   Stack type : decreasing (equal allowed)
    *   Operator in while loop : stackTop < current
    *   Assignment Position : inside while loop

    Let's start with this example. We are given with the following array and we need
    to find the next greater elements for each of items of the array.

    nums = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]

    Next greater elements (what is the next greater element for the item at this index) -
    nextGreaterElements = [null, 9, 5, 9, 5, 9, 12, 12, 12, null]

    On the place of writing the element itself, we can also write its index -
    nextGreaterIndexes = [-1, 6, 3, 6, 5, 6, 9, 9, 9, -1] (for 13 and 12), because there
    are no greater elements after themselves, we use -1, an invalid index value of the
    next greater element. You could use null or nums.length as well.
    """

    # initialize an empty stack
    stack = deque()

    # initialize nextGreater array, this array hold the output
    # initialize all the elements are -1 (invalid value)
    nextGreater = [-1] * len(nums)

    # iterate through all the elements of the array
    for idx, val in enumerate(nums):
        # while loop runs until the stack is not empty AND
        # the element represented by stack top is STRICTLY SMALLER than the current element
        # This means, the stack will always be monotonic non increasing (type 4)
        while stack and nums[stack[-1]] < val:
            # pop out the top of the stack, it represents the index of the item
            # as given in the condition of the while loop above,
            # nextGreater element of stackTop is the element at index i
            nextGreater[stack.pop()] = val

        # push the current index
        stack.append(idx)

    return nextGreater


def findPreviousGreater(nums: list[int]) -> list[int]:
    """
    3.  Strictly decreasing - every element of the stack is strictly smaller than the previous element.

    *   Stack type : decreasing (strict)
    *   Operator in while loop : stackTop <= current
    *   Assignment Position : outside while loop

    This time we want to find the previous greater elements. One option is to iterate from arr.length - 1
    to 0 and use the same logic as above in the opposite direction. In order to keep things simple,
    I rather like another flavour of the template above where we add three more lines after the while
    loop to get the previous greater element. Let's see how to do that.

    arr = [13, 8, 1, 5, 2, 5, 9, 7, 6, 12]

    Previous greater elements -
    previousGreaterElements = [null, 13, 8, 8, 5, 8, 13, 9, 7, 13]
    nextGreaterIndexes = [-1, 0, 1, 1, 3, 1, 0, 6, 7, 0]
    """

    stack = deque()
    prevGreater = [-1] * len(nums)

    for idx, val in enumerate(nums):
        #  while loop runs until the stack is not empty AND
        #  the element represented by stack top is SMALLER OR EQUAL to the current element
        #  This means, the stack will always be strictly decreasing (type 3) - because elements are popped when they are equal
        #  so equal elements will never stay in the stack (definition of strictly decreasing stack)
        while stack and nums[stack[-1]] <= val:
            # pop out the top of the stack, it represents the index of the item
            stack.pop()

        # after the while loop, only the elements which are greater than the current element are left in stack
        # this means we can confidently decide the previous greater element of the current element i, that's stack top
        if stack:
            prevGreater[idx] = nums[stack[-1]]

        # push the current index
        stack.append(idx)

    return prevGreater


def findNextSmaller(nums: list[int]) -> list[int]:
    """
    2.  Increasing - every element of the stack is greater than or equal to the previous element.

    *   Stack type : increasing (equal allowed)
    *   Operator in while loop : stackTop > current
    *   Assignment Position : inside while loop
    """
    stack = deque()
    nextSmaller = [-1] * len(nums)

    for idx, val in enumerate(nums):
        # while loop runs until the stack is not empty AND
        # the element represented by stack top is STRICTLY LARGER than the current element
        # This means, the stack will always be monotonic non decreasing (type 2)
        while stack and nums[stack[-1]] > val:
            # as given in the condition of the while loop above,
            # nextSmaller element of stackTop is the element at index i
            nextSmaller[stack.pop()] = val

        # push the current index
        stack.append(idx)

    return nextSmaller


def findPreviousSmaller(nums: list[int]) -> list[int]:
    """
    1.  Strictly increasing - every element of the stack is strictly greater than the previous element.

    *   Stack type : increasing (strict)
    *   Operator in while loop : stackTop >= current
    *   Assignment Position : outside while loop
    """
    stack = deque()
    prevSmaller = [-1] * len(nums)

    for idx, val in enumerate(nums):
        # while loop runs until the stack is not empty AND
        # the element represented by stack top is LARGER OR EQUAL to the current element
        # This means, the stack will always be monotonic strictly increasing (type 1)
        while stack and nums[stack[-1]] >= val:
            stack.pop()
        if stack:
            prevSmaller[idx] = nums[stack[-1]]
        stack.append(idx)
    return prevSmaller


def findNextAndPreviousGreater(nums: list[int]) -> list[int]:
    stack = deque()
    prevGreater, nextGreater = [-1] * len(nums), [-1] * len(nums)

    for idx, val in enumerate(nums):

        while stack and nums[stack[-1]] <= val:
            nextGreater[stack.pop()] = val
        if stack:
            prevGreater[idx] = nums[stack[-1]]
        stack.append(idx)

    return [prevGreater, nextGreater]


def findNextAndPreviousSmaller(nums: list[int]) -> list[int]:
    stack = deque()
    prevSmaller, nextSmaller = [-1] * len(nums), [-1] * len(nums)

    for idx, val in enumerate(nums):

        while stack and nums[stack[-1]] >= val:
            nextSmaller[stack.pop()] = val
        if stack:
            prevSmaller[idx] = nums[stack[-1]]
        stack.append(idx)

    return [prevSmaller, nextSmaller]


def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    """
    LeetCode Problem: 496. Next Greater Element I

    Link: https://leetcode.com/problems/next-greater-element-i/description/
    """

    stack, nextGreater = deque(), dict.fromkeys(nums2, -1)
    for val in nums2:

        # while stack and
        # the right most value of stack
        # is less than current value
        while stack and stack[-1] < val:

            # then pop the value and
            # assign the current value
            # to the key of the pop value
            nextGreater[stack.pop()] = val
        stack.append(val)

    return [nextGreater[val] for val in nums1]

    # or as a generator (faster than list)
    # return (nextGreater[val] for val in nums1)

    # or using map
    # return map(nextGreater.get, nums1)


def nextGreaterElements(self, nums: list[int]) -> list[int]:
    """
    LeetCode Problem: 503. Next Greater Element II

    Link: https://leetcode.com/problems/next-greater-element-ii/description/

    Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]),
    return the next greater number for every element in nums.

    The next greater number of a number x is the first greater number to its traversing-order next in the array,
    which means you could search circularly to find its next greater number. If it doesn't exist,
    return -1 for this number.

    Solution
    It is essentially the same problem as the one described above. There is an additional twist of being a circular array.
    Which means, the next greater element for the last element in the array could be the first of the previous elements
    if it is bigger. (the array wraps around)

    To solve this problem, we run the parent for loop two times.

    Problem type    -   next greater
    Stack type      -   monotonic decreasing
    Operator        -   <
    """

    stack, ans = deque(), [-1] * len(nums)

    for idx in list(range(len(nums))) * 2:

        # Check if stack and right most value from
        # stack which indicate idx which index in
        # nums is less than current index
        while stack and nums[stack[-1]] < nums[idx]:

            # If so then use right most value from stack
            # as index and assign current value to that index
            ans[stack.pop()] = nums[idx]

        # Store the index of the value
        # as it is the same list
        stack.append(idx)

    return ans


def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    """
    LeetCode Problem: 739. Daily Temperatures

    Link: https://leetcode.com/problems/daily-temperatures/

    Problem type    -   next greater
    Stack type      -   monotonic decreasing
    Operator        -   <
    """
    stack, ans = deque(), [0] * len(temperatures)

    for idx, val in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < val:
            ans[stack.pop()] = idx - stack[-1]
        stack.append(idx)

    return ans


def findBuildings(self, heights: list[int]) -> list[int]:
    """
    *** Premium
    Monotonic Stack - Strictly decreasing
    Que link: https://leetcode.ca/2021-04-14-1762-Buildings-With-an-Ocean-View/

    A building has ocean view if all buildings on its right are smaller than this building.

    Problem type    -   next greater
    Stack type      -   monotonic strictly decreasing
    Operator        -   <=
    """
    stack = deque()

    for idx, val in enumerate(heights):
        while stack and heights[stack[-1]] <= val:
            stack.pop()
        stack.append(idx)

    return stack


def find132pattern(self, nums: list[int]) -> bool:
    """
    We consider the largest possible last_number so that the nums[i] < last_number
    check has the largest possible range of values of nums[i] for it to return true.
    (We can guarantee that last_number is the largest possible second number for the
    current index since we popped it from stack, which is monotonically decreasing.)
    Consider the following example:

    nums = [ 1, 4, 3, 2 ]

    When idx = 3, stack = [ ], last_number = -inf
    When idx = 2, stack = [2], last_number = -inf
    When idx = 1, stack = [3], last_number = 2
    When idx = 0, stack = [4], last_number = 3

    132 pattern found: ( 1, 4, 3 )

    Problem type    -   next greater
    Stack type      -   monotonic decreasing
    Operator        -   <
    """
    if len(nums) < 3:
        return False

    stack, last_number = [], -inf

    for n in nums[::-1]:
        if n < last_number:
            # lowest number will be n
            # biggest number will be (middle one) in the stack
            # second big number will be last_number
            return True

        while stack and stack[-1] < n:
            last_number = stack.pop()
        stack.append(n)
    return False


# Greater
# print(findNextGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
# print(findPreviousGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
# print(findNextAndPreviousGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))

# Smaller
# print(findNextSmaller([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
# print(findPreviousSmaller([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
# print(findNextAndPreviousSmaller([13, 8, 1, 5, 2, 5, 9, 7, 6, 12]))
print(findNextAndPreviousSmaller([2, 1, 5, 6, 2, 3]))

# LeetCode Problems
# print(nextGreaterElement(0, nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
# print(nextGreaterElements(0, nums=[5, 4, 3, 2, 1]))  # [-1,5,5,5,5]
# print(dailyTemperatures(0, [73, 74, 75, 71, 69, 72, 76, 73]))
# print(findBuildings(0, heights=[4, 2, 3, 1]))  # [0,2,3]
# print(find132pattern(0, [1, 4, 3, 2]))  # true
