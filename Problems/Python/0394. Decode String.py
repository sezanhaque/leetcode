class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            # while we are not getting ']'
            # it means we can add the chars
            # to stack
            if char != "]":
                stack.append(char)

            # else we know we need to multiply
            # strings as per stack
            else:
                curr_str = ""
                # while we are not facing '['
                # if means we can add the pop
                # char from stack and add it to
                # curr_str, remember we need to
                # first add pop char then add the
                # curr_str so that the order of
                # string is maintained
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str

                # pop '['
                stack.pop()

                multiplier = ""

                # now we are getting the number, which
                # will decide how many times we should
                # multiply our str.
                # For this, we also need to firstly add
                # the pop char then add multiplier
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                # lastly we are multiplying the curr_str
                # with multiplier and append it to stack
                # so that we can use this multiplied str
                # if we need to do this.
                stack.append(int(multiplier) * curr_str)

        return "".join(stack)


obj = Solution()
print(obj.decodeString("3[a2[c]]"))
