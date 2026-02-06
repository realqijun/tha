stack = []
top = -1

def simple_stack(fun, item):
    if fun == 'PUSH':
        stack[top + 1] = item
        top = top + 1
    elif fun == 'POP':
        if top == -1:
            return None
        ret = stack[top]
        stack[top] = None
        top = top - 1
        return ret
    elif fun == 'PEEK':
        return stack[top]

