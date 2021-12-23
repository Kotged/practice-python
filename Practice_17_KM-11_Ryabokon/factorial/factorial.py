def fact(n):
    if n < 0:
        print('Error. The number must be natural')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        res = n * fact(n-1)
        return res