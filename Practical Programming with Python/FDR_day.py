def days_difference(day1: int, day2: int) -> int:

    '''
    (int, int) -> int

    Returns the number of days between days of the year, day1 and day2,
    which fall in the range 365

    >>> days_difference(100, 90)
    -10
    >>> days_difference(90, 100)
    10
        >>> days_difference(100,100)
    0
    '''
    return day2 - day1

def get_weekday(current_weekday: int, days_ahead: int) -> int:
    '''
    returns which day of the week it will be after day_ahead days from
    current weekday

    current_weekday is the day of the week indicated using an integer
    starting from sunday as 1, monday as 2 and likewise

    days_ahead are the number of days after today

    >>> get_weekday(3,1)
    4
    >>> get_weekday(6,1)
    7
    >>> get_weekday(7,1)
    1
    >>> get_weekday(7,0)
    7
    >>> get_weekday(7,7)
    7
    >>> get_weekday(2, 70)
    2
    '''
    return (current_weekday + days_ahead - 1) % 7 + 1

def get_birthday_weekday(current_weekday, current_doy, birthday_doy):
    '''
    (integer, integer, integer) -> integer

    Returns weekday for the birthday_doy when given current_weekday and
    current_doy.

    birthday_doy is the day of the year when the birthday falls and is in the range
    1-365.
    current_doy is the current day of the year in the range 1-365
    current_weekday is the day of the week starting from Sunday as 1, saturday as
    7 and likewise.

    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    '''
    diff = days_difference(current_doy, birthday_doy)
    return get_weekday(current_weekday, diff)
