def different(a, b):
    '''(number, number) -> bool

    Returns True if a and b are different else False

    >>> different(10, 12)
    True
    >>> different(10.0, 10)
    False
    '''
    return not a == b

print(different(10, 12))
print(different(10.0, 10))
