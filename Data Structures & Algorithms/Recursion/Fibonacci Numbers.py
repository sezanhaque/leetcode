def fibonacci(num: int) -> int:
    """
    Function for nth fibonacci
    number - Space Optimization
    Taking 1st two fibonacci numbers as 0 and 1
    """
    if num < 0:
        print("Incorrect input")
        return
    elif num == 0:
        return num
    elif num == 1:
        return num
    else:
        a, b = 0, 1
        for _ in range(1, num):
            curr = a + b
            a, b = b, curr
        return b


# track the root node of the recursion
# so that we don't need to go to same node again and again
seen = {}


def fibonacciWithRecursion(num: int) -> int:
    """
    Function for nth fibonacci using Recursion
    Taking 1st two fibonacci numbers as 0 and 1
    """
    if num < 0:
        print("Incorrect input")
        return
    elif num < 2:
        return num
    elif num in seen:
        return seen[num]
    seen[num] = fibonacciWithRecursion(num - 1) + fibonacciWithRecursion(num - 2)
    return seen[num]


fibArray = [0, 1]


def fibonacciWithDP(num: int) -> int:
    """
    Function for nth fibonacci using Dynamic Programming
    Taking 1st two fibonacci numbers as 0 and 1
    """
    if num < 0:
        print("Incorrect input")
        return
    elif num < len(fibArray):
        return fibArray[num]
    else:
        fibArray.append(fibonacciWithDP(num - 1) + fibonacciWithDP(num - 2))
        return fibArray[num]


print(fibonacci(100))
print(fibonacciWithRecursion(100))
print(fibonacciWithDP(100), fibArray)
