from os import path

# PYTHON VERSION:
GAME_PYTHON_VERSION = '3.7.9'

# GAME INFO:
GAME_TITLE = 'BATALHA NAVAL'
GAME_AUTHOR = 'Leandro Cardoso'
GAME_DESCRIPTION = f'''Bem vindo(a) a Batalha Naval !!!
Criado por {GAME_AUTHOR}.
Tecnologias: Python.

Um jogo de batalha naval para rodar no terminal (CMD).
Esse projeto foi desenvolvido como trabalho da Universidade de 
Vassouras, curso de Engenharia de Software, disciplina de Pensamento 
Computacional, ministrada pelo professor João Coelho.

DICAS:
Os navios são representados por numeros.
Os numeros também representam o tamanho deles, como uma dica.
O "Battleship" por exemplo tem 4 espaços de tamanho.
Ex: "4  4  4  4" <- Sendo essa a sua representação.
Mais informações na legenda acima.'''

# GAME PATHS:
GAME_SFX_PATH = path.abspath('.\game\sfx') + '\\'

# COLORS:
COLOR_RESET = '\033[m' # reset
COLOR_SUCCESS = '\033[32m' # green
COLOR_FAIL = '\033[31m' # red
COLOR_TEXT = '\033[33m' # yellow
COLOR_INPUT = '\033[30;44m' # bg blue
COLOR_WATER = '\033[34m' # blue
COLOR_SHIP = '\033[37m' # white
