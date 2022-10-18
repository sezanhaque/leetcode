def containsDuplicate(self, nums: list[int]) -> bool:
    """
    Here we are using result = set() instead of result = [] (list)
    because set() is faster than list in case of checking the item is present in the set.
    """
    result = set()
    for i in nums:
        if i in result:
            return True
        result.add(i)
    return False


print(containsDuplicate(0, [1, 2, 3, 1]))
