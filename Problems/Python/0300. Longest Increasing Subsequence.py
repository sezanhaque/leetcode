from bisect import bisect_left


def pathOfLIS(self, nums: list[int]):
    sub = []
    subIndex = []  # Store index instead of value for tracing path purpose
    path = [-1] * len(nums)  # path[i] point to the index of previous number in LIS
    
    for i, val in enumerate(nums):
        if len(sub) == 0 or sub[-1] < val:
            path[i] = -1 if len(subIndex) == 0 else subIndex[-1]
            sub.append(val)
            subIndex.append(i)
        else:
            idx = bisect_left(
                sub, val
            )  # Find the index of the smallest number >= val, replace that number with val
            path[i] = -1 if idx == 0 else subIndex[idx - 1]
            sub[idx] = val
            subIndex[idx] = i

    ans = []
    t = subIndex[-1]
    while t >= 0:
        ans.append(nums[t])
        t = path[t]
    return ans[::-1]


print(pathOfLIS(0, [2, 6, 8, 3, 4, 5, 1]))  # [2, 3, 4, 5]
