def tail(n):
    if n == 0:
        return

    print(n)
    tail(n - 1)

tail(5)
'''In tail recursion, the processing is done before the recursive call.
The recursive call is the last statement in the function.'''