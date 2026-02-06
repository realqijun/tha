def first_uniq_char(s: str):
    d = {}
    for c in s:
        if d.get(c) is None: # use get to avoid KeyError
            d[c] = 1
        else:
            d[c] = d[c] + 1 # increment count
    for c in s:
        if d[c] == 1:
            return c
    return None

print(first_uniq_char("hello"))
