def factorial_tail(n, accumulator=1):
    if n == 0 or n == 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)


print(factorial_tail(5))  
