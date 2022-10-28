"""
Sub array
Prefix sum
"""


def sumOddLengthSubarrays(self, arr: list[int]) -> int:
    length = len(arr)
    sums, left, right = 0, 0, 1
    for i in range(0, length, 2):
        left, right = 0, i
        while right < length:
            sums += sum(arr[left : right + 1])
            left += 1
            right += 1
    return sums


def sumOddLengthSubarrays(self, arr: list[int]) -> int:
    result = 0
    length = len(arr)

    for idx, val in enumerate(arr):
        """
        Start = how many sub arrays will be start with the value
        End = how many sub arrays will end with the value
        Total = how many times the value will be there in all sub arrays
        Odd = We have to get only the odd length of sub arrays so we divide them by 2
        Result = multiply the Odd with the array index value and sum with previous value
        """
        start = length - idx
        end = idx + 1
        total = start * end + 1
        odd = total // 2
        result += odd * val

    return result


def sumOddLengthSubarrays(self, arr: list[int]) -> int:
    return sum(((idx + 1) * (len(arr) - idx) + 1) // 2 * value for idx, value in enumerate(arr))


# def sumOddLengthSubarrays(self, arr: list[int]) -> int:
#     res = 0
#     freq = 0
#     n = len(arr)
#     for i in range(n):
#         freq = freq - (i + 1) // 2 + (n - i + 1) // 2
#         res += freq * arr[i]
#     return res


print(sumOddLengthSubarrays(0, [1, 2]))
print(sumOddLengthSubarrays(0, [1, 4, 2, 5, 3]))
print(sumOddLengthSubarrays(0, [10, 11, 12]))
