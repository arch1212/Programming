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

def above_freezing(celsius):
    '''(float) -> bool

    Returns True when celsius is above freezing temperature, otherwise,
    it returns false
    
    >>> above_freezing(10)
    True
    >>> above_freezing(-10)
    False
    '''
    return celsius > 0

