def ordinal(n: int):
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

#solution: https://stackoverflow.com/questions/69613797/is-there-any-easier-way-to-put-word-after-numbers-in-string
