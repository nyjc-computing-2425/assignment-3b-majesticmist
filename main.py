stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
x = stdform.find('x')
mantissa = stdform[:x]
exponent = stdform[x+4:]

print(f'This number in E notation is {mantissa}E{exponent}.' )