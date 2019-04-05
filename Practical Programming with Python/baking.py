import temperature_program as tp

def get_preheating_instructions(fahrenheit):
    '''(float) -> str

    Return instructions for preheating the oven in fahrenheit and
    celsius degrees

    >>> get_preheating_instructions(500)
    'Preheat the oven to 500 degrees F  (260.0 degrees C).'
    '''
    cels =  tp.convert_to_celsius(fahrenheit)
    fahr = fahrenheit
    return f'Preheat oven to {fahrenheit} degrees F ({cels} degrees C).'
if __name__ == '__main__':
    fahr = float(input('Enter the baking temperature in degrees fahrenheit: '))
    print(get_preheating_instructions(fahr))    
