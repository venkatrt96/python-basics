# String Methods
course = 'Python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('for'))
print(course.replace('beginners', 'absolute beginners'))

print('Python' in course)
print(course.title())

# Arithmetic Operations
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 * 3)
print(10 ** 3) # Power

x = 10
x += 10
print(x)

# Operator Precedence
# exponentiation > Multiplication or Division > Add or Subtract
# solution paranthesis

# Math Functions
x = 2.9
print(round(x))
print(abs(-x))

import math # Math module
print(math.ceil(x))
print(math.floor(x))

# If Statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print('Drink plenty of water')
elif is_cold:
    print("It's a cold day")
    print('Wear warm clothes')
else:
    print("It's a lovely day")
print('Enjoy your day')

# Logical Operators
has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
    print('Elligible for loan')

has_high_income = False
has_good_credit = True

if has_good_credit or has_high_income:
    print('Elligible for loan')

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('Elligible for loan')

# Comparison Operators
temp = 35

if temp != 30:
    print('It is a hot day')
else:
    print('It is not a hot day')

# While Loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('Done')

# For Loops
for item in 'Python':
    print(item)

for item in ['One', 'Two']:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for item in range(5, 10, 2):
    print(item)

# Nested Loops
for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')