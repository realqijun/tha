stack = []
top = -1

def simple_stack(fun, item):
    if fun == 'PUSH':
        stack[top + 1] = item  # put the item on top of the stack
        top = top + 1  # increment top
        return None

    elif fun == 'POP':
        if top == -1:
            return None  # return None if stack is empty

        ret = stack[top]
        stack[top] = None
        top = top - 1  # decrement top
        return ret

    elif fun == 'PEEK':
        if top == -1:
            return None  # return None if stack is empty
        return stack[top]
