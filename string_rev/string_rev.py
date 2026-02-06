def string_rev(s: str):
    arr = []
    for i in s:
        arr.append(i)
    res = ''
    for c in arr:
        res = c + res
    return res
