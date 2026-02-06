def helper(x, y, iter):
    if x < y:
        return x, iter
    return helper(x - y, y, iter + 1)

def div_mod(x, y):
    return helper(x, y, 0)

print(divmod(10, 3))