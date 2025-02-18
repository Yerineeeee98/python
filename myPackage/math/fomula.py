pi = 3.14

def my_max(a, b):
    if a > b:
        return a
    else:
        return b


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1) * n