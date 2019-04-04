def repeat(s: str, n: int) -> str:
    """ Return s repeated n times; if n is negative, return the empty string.
    >>> repeat('yes', 4)
    'yesyesyesyes'
    >>> repeat('no', 0)
    >>> repeat('no', -2)
    >>> repeat('yesnomaybe', 3)
    """
    return s*n

print(repeat('yes', 4))
print(repeat('no', 0))
print(repeat('no', -2))
print(repeat('yesnomaybe', 3))
