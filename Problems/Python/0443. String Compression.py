from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        left = right = count = 0

        while left < len(chars):
            while right < len(chars) and chars[left] == chars[right]:
                count += 1
                right += 1

            # if count of char is greater than 1
            # then add the count
            if count > 1:
                res.append(chars[left])

                # we will add the digits of a number separately
                for n in str(count):
                    res.append(n)
            else:
                res.append(chars[left])

            count = 0
            left = right

        chars[:] = res

        return len(chars)


obj = Solution()
print(obj.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(obj.compress(["a"]))
print(obj.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(obj.compress(["a", "a", "a", "b", "b", "a", "a"]))  # ["a","3","b","2","a","2"]
