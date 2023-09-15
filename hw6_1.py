from sys import argv
from isValidDate import date_exist as dex

value = argv[1]
print('Такая дата существует') if dex(value) else print('Такая дата не существует')
