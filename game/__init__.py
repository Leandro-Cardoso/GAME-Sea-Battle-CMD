import pandas as pd
from os import system

ships = {
    5 : {'C' : 'carrier'},
    4 : {'B' : 'battleship'},
    3 : {'S' : 'submarine'},
    2 : {'D' : 'destroyer'},
    1 : {'' : ''}
}

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

for i, col in enumerate(columns):
    columns[i] = '\033[33m' + col + '\033[m'
for i, line in enumerate(lines):
    lines[i] = '\033[33m' + line + '\033[m'

field = [
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', '', '']
]

for i in range(10):
    for j in range(10):
        field[i][j] = '\033[34mX\033[m'

table = pd.DataFrame(data = field, index = lines, columns = columns)

system('cls')
print(table)
