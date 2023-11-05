from os import system

from field import Field
from score import Score

ships = {
    5 : {'C' : 'carrier'},
    4 : {'B' : 'battleship'},
    3 : {'S' : 'submarine'},
    2 : {'D' : 'destroyer'},
    1 : {'' : ''}
}

system('cls')

field = Field()
field.render()

score = Score()
score.render()
