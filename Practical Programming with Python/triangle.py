def area(base, height):
    '''
    (number, number) -> float

    Returns the area of the triangle with base and height of the triangle

    >>> area(10, 20)
    100.0
    >>> area(100, 5)
    250.0
    '''
    return base*height/2

def perimeter(side1, side2, side3):
    '''
    (number, number, number) -> number

    Returns the perimeter of the triangle with all three sides, side1, side2 and
    side3

    >>> perimeter(10, 12, 14)
    36
    >>> perimeter(8, 9, 11)
    28
    '''
    return side1 + side2 + side3

def semi_perimeter(side1, side2, side3):
    '''
    (number, number, number) -> float

    Returns the semi-perimeter using all three sides, side1, side2, and side3

    >>> semi_perimeter(10, 12, 14)
    18.0
    >>> semi_perimeter(8, 9, 11)
    14.0
    '''
    return perimeter(side1, side2, side3)/2
