def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    print(mergeSort(nums))

def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    red, white, blue = nums.count(0), nums.count(1), nums.count(2)
    nums[:red] = [0] * red
    nums[red:red + white] = [1] * white
    nums[red + white:] = [2] * blue
    return nums

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        left = arr[:mid]

        # into 2 halves
        right = arr[mid:]

        # Sorting the first half
        mergeSort(left)

        # Sorting the second half
        mergeSort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


print(sortColors(0, [2, 0, 2, 1, 1, 0]))
