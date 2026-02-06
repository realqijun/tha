def helper(x, y, iter):
    if x < y:
        return x, iter
    return helper(x - y, y, iter + 1)

def div_mod(x, y):
    helper(x, y, 0)
