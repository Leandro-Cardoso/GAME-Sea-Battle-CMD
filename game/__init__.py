import pandas as pd
from os import system

from models import Field

ships = {
    5 : {'C' : 'carrier'},
    4 : {'B' : 'battleship'},
    3 : {'S' : 'submarine'},
    2 : {'D' : 'destroyer'},
    1 : {'' : ''}
}

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

table = pd.DataFrame(data = '+', index = lines, columns = columns)

system('cls')
#print(table)

#msg = '\nAguarde...\n'
#print(f'\033[33m{msg}\033[m')

field = Field()
field.render_field()
