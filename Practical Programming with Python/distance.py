def convert_to_miles(km_distance):
    '''(number) -> float

    Returns the number of miles in km_distance

    >>> convert_to_miles(16)
    10.0
    >>> convert_to_miles(32)
    20.0
    '''
    return km_distance/1.6

print(convert_to_miles(16))
print(convert_to_miles(32))
