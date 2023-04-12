class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for char in path.split("/"):
            # if we have stack and
            # we need to go back then
            # pop from stack
            if stack and char == "..":
                stack.pop()

            # else if char not in these
            # then we can append it to stack
            elif char not in ["", ".", ".."]:
                stack.append(char)

        return "/" + "/".join(stack)


obj = Solution()
print(obj.simplifyPath("/home/"))
