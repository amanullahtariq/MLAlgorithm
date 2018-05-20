# The Fibonacci Sequence
# The Fibonacci sequence begins with fibonacci(0) = 0  and  fibonacci(1) = 1 as its respective first and second terms. After these first two elements, each subsequent element is equal to the sum of the previous two elements.


def fibonacci(n):
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n- 2)



fib_list = []
for i in range(0, 11):
    fib_list.append(fibonacci(i))

print(fib_list)