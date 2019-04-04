def convert_to_celsius(fahrenheit):
    '''
    (number) -> float

    returns temperature in celsius using fahrenheit temperature

    >>> convert_to_celsius(212)
    100.0
    >>> convert_to_celsius(112)
    44.4
    '''
    return (fahrenheit - 32) * 5/9


print(convert_to_celsius(80))
print(convert_to_celsius(78))
