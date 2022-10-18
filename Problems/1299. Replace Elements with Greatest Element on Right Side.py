def replaceElements(self, arr: list[int]) -> list[int]:
    # if len(arr) < 2:
    #     return -1
    # for i in range(len(arr) - 1):
    #     max_element = -1
    #     for j in range(i + 1, len(arr)):
    #         if arr[j] > max_element:
    #             max_element = arr[j]
    #         arr[i] = max_element
    # arr[-1] = -1
    # return arr
    max_value = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_value = max_value, max(max_value, arr[i])
    return arr


print(replaceElements(0, [17, 18, 5, 4, 6, 1]))
print(replaceElements(0, [400]))
