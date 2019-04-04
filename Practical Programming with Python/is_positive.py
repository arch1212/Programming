def is_positive(number):
    '''
    (float) -> bool

    Return True iff number is positive
     
    >>> is_positive(10)
    True

    >>> is_positive(-19.09)
    False
    '''
    return  number > 0

print('10 is positive:', is_positive(10))
print('-19.09 is positive:', is_positive(-19.09))
