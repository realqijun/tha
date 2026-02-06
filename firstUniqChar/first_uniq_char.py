def first_uniq_char(s: str):
    d = {}
    for c in s:
        if d[c] is None:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    for c in s:
        if d[c] == 1:
            return c
    return None
