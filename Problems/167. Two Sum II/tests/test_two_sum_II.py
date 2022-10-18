def twoSum(self, numbers, target):
    """
    Solution 1: HashMap

    We need to find 2 numbers REMAINING, VALUE so that REMAINING + VALUE = TARGET.
    We need a HashMap data structure to store elements in the past, let name it seen.
    The idea is that we iterate b as each element in numbers, we check if we found a (where REMAINING = TARGET - VALUE) in the past.
    If a exists in seen then we already found 2 numbers REMAINING and VALUE, so that REMAINING + VALUE = TARGET, just output their indices.
    Else add b to the seen.
    """
    seen = {}
    for i, value in enumerate(numbers):
        remaining = target - numbers[i]

        if remaining in seen:
            return [seen[remaining] + 1, i + 1]

        seen[value] = i

        

def test_two_sum():
    assert twoSum(0, [2, 7, 11, 15], 9) == [1, 2]