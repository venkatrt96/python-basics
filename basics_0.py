# Basic print statement
print('I am Venkat')
print('*' * 10)

# Variables
price = 10
rating = 4.9
name = 'Venkat'
is_published = True
print(price)

# Receiving Input
name = input('What is your name ? ')
print('Hi ' + name)

# Type Conversion
birth_year = input('What is your birth year ? ')
print(type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
# int()
# float()
# bool()
print('Your age is ', age)

# Strings
course = "Python's Course for beginners"
course = '''
Hi John,

Here is our first email to you.

Thank You
'''
course = 'Python for "beginners"'

print(course)
print(course[1])
print(course[-2])
print(course[0:3])
print(course[1:])
print(course[:5])
print(course[:])

name = 'Jennifer'
print(name[1:-1])

# Copy a variable
another = course[:]
print(another)

# Formatted Strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)
