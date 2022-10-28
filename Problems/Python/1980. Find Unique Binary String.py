def findDifferentBinaryString(self, nums: list[str]) -> str:
    if len(nums) < 2:
        return "0" if nums[0] == "1" else "1"

    bin_str = []
    len_of_nums = len(nums[0])
    for _, v in enumerate(nums):
        for _, _v in enumerate(v):
            bin_str.append(_v)

    for i in range(len(bin_str)):
        for j in range(len(bin_str)):
            list_of_str = bin_str[j : j + len_of_nums - 1]
            picked_str = ""
            for _, v in enumerate(list_of_str):
                picked_str += v
            if (
                bin_str[i] + picked_str not in nums
                and len(bin_str[i] + picked_str) == len_of_nums
            ):
                return bin_str[i] + picked_str


def findDifferentBinaryString(self, nums: list[str]) -> str:
    """
    Fast Solution
    """
    size = len(nums)
    num = 0
    while True:
        """
        Create a binary string of length size
        where the number will be increased by 1
        """
        s = f"{num:0{size}b}"
        print(s)
        if s not in nums:
            return s
        num += 1


def findDifferentBinaryString(self, nums):
    ans = ""
    for i, num in enumerate(nums):
        ans += "1" if (num[i] == "0") else "0"
    return ans

def findDifferentBinaryString(self, nums):
    return ''.join(['1' if num[i]=='0' else '0' for i,num in enumerate(nums)])


# print(findDifferentBinaryString(0, ["01", "10"]))
# print(findDifferentBinaryString(0, ["00", "01"]))
print(findDifferentBinaryString(0, ["111", "011", "001"]))
# print(findDifferentBinaryString(0, ["0"]))
