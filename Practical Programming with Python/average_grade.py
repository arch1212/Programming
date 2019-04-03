def avg_grade(grade1, grade2, grade3):
    '''(number, number, number) -> number

    Returns the average of three grades, grade1, grade2, and grade3

    >>> avg_grade(0, 100, 98)
    66.0
    >>> avg_grade(0, 0, 0)
    0.0
    '''
    return (grade1 + grade2 + grade3)/3

def average_best_three(grade1, grade2, grade3, grade4):
    '''(number, number, number, number) ->

    Returns the average of best 3 of 4 grade scores, grade1, grade2, grade3
    and grade4
    
    >>> average_best_three(20, 30, 40, 50)
    40.0
    >>> average_best_three(10, 20, 20, 10)
    16.666666666
    >>> average_best_three(0, 0, 0, 9)
    3.0
    '''
    return max(avg_grade(grade1, grade2, grade3),
               avg_grade(grade2, grade3, grade4),
               avg_grade(grade1, grade3, grade4),
               avg_grade(grade1, grade2, grade4))
    
print(average_best_three(0, 0, 0, 9))
print(average_best_three(10, 20, 20, 10))
