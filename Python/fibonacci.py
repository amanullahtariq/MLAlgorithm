def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    num1 = fibonacci(n - 1)
    num2 = fibonacci(n- 2)


    return num1 + num2



fib_list = []
for i in range(0, 11):
    fib_list.append(fibonacci(i))

print(fib_list)