def string_rev(s: str):
    res = ''
    i = 0
    while i < len(s):
        res = s[i] + res
        i += 1
    return res

print(string_rev('hello'))
