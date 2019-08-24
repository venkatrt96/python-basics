# Modules
import utils # importing Modules
from utils import lbs_to_kg # importing specific Modules
print(utils.kg_to_lbs(20))
print(lbs_to_kg(20))

# Packages
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
calc_shipping()

# Generating Random Values
import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Smaith', 'Carl', 'Wayne']
leader = random.choice(members)
print(leader)

#  Working with Directories
from pathlib import Path
path = Path('ecommerce')
print(path.exists())
path1 = Path('emails')
# path1.mkdir()
# path1.rmdir()
path2 = Path()
for file in path2.glob('*.py'):
    print(file)

# Pypi
import openpyxl as xl
workbook = xl.load_workbook('transactions.xlsx')
sheet = workbook['Sheet1']
cell = sheet['a1']
cell = sheet.cell(1, 1) # same as above line
print(cell.value)
