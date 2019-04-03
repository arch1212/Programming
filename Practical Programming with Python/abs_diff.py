def abs_diff(number1, number2):
    '''
    (number, number) -> number

    returns the absolute difference between number1 and number2

    >>> abs_diff(10, 20)
    10
    >>> abs_diff(20, 10)
    10
    >>> abs_diff(10, 10)
    0
    >>> abs_diff(-10, 0)
    10
    '''
    return abs(number1 - number2)

print(abs_diff(10, 20))
print(abs_diff(20, 10))
print(abs_diff(10, 10))
print(abs_diff(-10, 0))
