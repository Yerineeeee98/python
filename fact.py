def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

def my_max(x, y):
    if x > y:
        return x
    else:
        return y
