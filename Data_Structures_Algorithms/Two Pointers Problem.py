class Solution:
    """
    Link: https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/

    Two-pointers is an extremely common technique used to solve array and string problems.
    It involves having two integer variables that both move along an iterable.
    In this article, we are focusing on arrays and strings. This means we will have two integers,
    usually named something like i and j, or left and right which each represent an index of the array or string.

    There are several ways to implement two-pointers. To start, let's look at the following method:

    Start one pointer at the first index 0 and the other pointer at the last index input.length - 1.
    Use a while loop until the pointers are equal to each other.
    At each iteration of the loop, move the pointers towards each other. This means either increment the pointer
    that started at the first index, decrement the pointer that started at the last index, or both.
    Deciding which pointers to move will depend on the problem we are trying to solve.

    Here's some pseudo-code illustrating the concept:

    function fn(arr):
        left = 0
        right = arr.length - 1

        while left < right:
            Do some logic here depending on the problem
            Do some more logic here to decide on one of the following:
                1. left++
                2. right--
                3. Both left++ and right--
    """

    def checkIfPalindrome(s: str) -> bool:
        """
        Return true if a given string is a palindrome, false otherwise.

        A string is a palindrome if it reads the same forwards as backwards.
        That means, after reversing it, it is still the same string.

        For example: "abcdcba", or "racecar".
        """
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def checkForTarget(nums: list[int], target: int) -> bool:
        """
        Given a sorted array of unique integers and a target integer,
        return true if there exists a pair of numbers that sum to target, false otherwise.
        This problem is similar to Two Sum.

        For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13,
        return true because 4 + 9 = 13.
        """
        left, right = 0, len(nums) - 1

        while left < right:
            curr = nums[left] + nums[right]
            if curr == target:
                return True
            if curr > target:
                right -= 1
            else:
                left += 1

        return False

    def combine(arr1: list[int], arr2: list[int]) -> list[int]:
        """
        Given two sorted integer arrays, return an array that combines both of them and is also sorted.
        """
        ans = []
        i = j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1

        while i < len(arr1):
            ans.append(arr1[i])
            i += 1

        while j < len(arr2):
            ans.append(arr2[j])
            j += 1

        return ans

    def isSubsequence(s: str, t: str) -> bool:
        """
        LeetCode 392. Is Subsequence.
        Link: https://leetcode.com/problems/is-subsequence/

        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

        A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
        of the characters without disturbing the relative positions of the remaining characters.
        (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
        """
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


print(Solution.checkIfPalindrome("racecar"))
print(Solution.checkForTarget([1, 2, 4, 6, 8, 9, 14, 15], 13))
print(Solution.combine([1, 4, 7, 20, 38], [3, 5, 6, 17]))
print(Solution.isSubsequence("abc", "ahbgdc"))
