from collections import deque
from functools import reduce


class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = deque()

        for val in s:
            ans.append(val) if not ans or val != ans[-1] else ans.pop()

        return "".join(ans)

    def removeDuplicates(self, s: str) -> str:
        return reduce(lambda ans, val: ans[:-1] if ans and ans[-1] == val else ans + val, s)


print(Solution.removeDuplicates(0, "abbaca"))
print(Solution.removeDuplicates(0, "azxxzy"))
