# Lists
names = ['One', 'Two', 'There']
print(names[-1])
print(names[2:])
print(names[:1])
print(names[:-1])
print(names[:]) # Returns a new list

# 2d Lists
# [
#     1 2 3
#     4 5 6
#     7 8 9
# ]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][0])
matrix[0][1] = 20
for row in matrix:
    for item in row:
        print(item)

# List Methods
numbers = [5, 2, 1, 7, 4]
numbers.append(20)
numbers.insert(1, 20)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.remove(20)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(0)
print(numbers)
print(f'Index: {numbers.index(2)}')
print(7 in numbers)
print(f'Count: {numbers.count(7)}')
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
number2 = numbers.copy()
print(number2)
numbers.clear()
print(numbers)

# Tuples
# Tuples are immutable
numbers = (1, 2, 3)
print(numbers.count(1))
print(numbers.index(1))

# Unpacking
coords = (1, 2, 3)
# coords[0] * coords[1] * coords[2]
# x = coords[0]
# y = coords[1]
# z = coords[2]
x, y, z = coords

# Dictionaries
customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}
print(customer['name'])
print(customer.get('name')) # doesnt throw error if accessing element not in dictionary
print(customer.get('birthday', '20 June'))
customer['birthday'] = '20th June'
print(customer.get('birthday'))

# Functions


def greet_user():
    print('Hi')


greet_user()

# Parameters


def greet_user(name):
    print(f'Hi {name}')


greet_user('John')

# Keyword Arguments


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')


greet_user(last_name='Smith', first_name='John')
# use positional argument first before keyword argument

# Return Statement


def square(number):
    return number * number


print(square(2))

# Exceptions
try:
    age = int('asd')
    print(age)
except ValueError:
    print('Invalid Value')

# Classes
class Point:


    def move(self):
        print('move')


    def draw(self):
        print('draw')


point = Point()
point.draw()
point.x = 20
point.y = 30
print(point.x, point.y)

# Constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')


    def draw(self):
        print('draw')

point = Point(20, 30)
print(point.x, point.y)

# Inheritance
class Mammel:
    def walk(self):
        print('walk')

class Dog(Mammel):
    def bark(self):
        print('bark')

class Cat(Mammel):
    pass

dog = Dog()
dog.walk()