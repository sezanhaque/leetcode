class Solution:
    """
    Link: https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/
    
    Sliding window is another common approach to solving problems related to arrays. 
    A sliding window is actually implemented using two-pointers! First, let's start by looking at the concept of a sub-array. 
    Given an array, a sub-array is just a section of the array. The elements need to be contiguous and in order. 
    For example, with the array [1, 2, 3, 4], the sub-arrays, grouped by length are:

    [1], [2], [3], [4]
    [1, 2], [2, 3], [3, 4]
    [1, 2, 3], [2, 3, 4]
    [1, 2, 3, 4]

    A sub-array can be defined by two indices, the start and end. 
    For example, with [1, 2, 3, 4], the sub-array [2, 3] has a starting index of 1 and an ending index of 2. 
    Let's call the starting index the left bound and the ending index the right bound. 
    Another name for sub-array in this context is "window", which we will use from now on.

    The idea behind the sliding window technique is to efficiently find the "best" window that fits some constraint. 
    Usually, the problem description will define what makes a window "better" (shorter length, larger sum etc.) and the constraint. 
    Imagine that a problem wanted the length of the longest sub-array with a sum less than or equal to k for an array with 
    positive numbers. In this case, the constraint is sum(window) <= k, and the longer the window, the better it is. 
    The general algorithm behind sliding window is:

    Define a pointer for the left and right bound that represents the current window, usually both of them starting at 0.
    Iterate over the array with the right bound to "add" elements to the window.
    Whenever the constraint is broken, in this example if the sum of the window exceeds k, then "remove" elements from 
    the window by incrementing the left bound until the condition is satisfied again.
    Here's some pseudo-code illustrating the concept:

    function fn(arr):
        left = 0
        for right in [0, arr.length - 1]:
            Do some logic to "add" element at arr[right] to window

            while left < right AND condition from problem not met:
                Do some logic to "remove" element at arr[left] from window
                left++

            Do some logic to update the answer
    """
    def findLength(nums: list[int], k: int) -> int:
        """
        Given an array of positive integers nums and an integer k,
        find the length of the longest sub-array whose sum is less than or equal to k.
        """
        left = curr = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans

    def findBinaryLength(s: str) -> int:
        """
        You are given a binary substring s (a string containing only "0" and "1").

        An operation involves flipping a "0" into a "1". What is the length of the longest
        substring containing only "1" after performing at most one operation?

        For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2,
        the string becomes 1111100111.
        """
        left = curr = ans = 0
        for right in range(len(s)):
            if s[right] == "0":
                curr += 1
            while curr > 1:
                if s[left] == "0":
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans


print(Solution.findLength([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
print(Solution.findBinaryLength("1101100111"))
