from os import system

from field import Field
from score import Score
from player import Player

from config import GAME_TITLE, GAME_DESCRIPTION

class Game():
    '''Create game file.'''
    def __init__(self) -> None:
        self.is_running = False
        self.player = Player()
        self.bot = Player(name = 'Bot', is_bot = True)
        self.score = Score()
        self.text_color = '\033[33m'
        self.error_color = '\033[31m'
        self.success_color = '\033[32m'

    def render_title(self) -> None:
        '''Render title and subtitles.'''
        # RESET SCREEN:
        system('cls')
        # TITLE:
        print(self.text_color + '=' * 69)
        n_simbols = 3
        simbol_l = '>' * n_simbols
        simbol_r = '<' * n_simbols
        print(f'{simbol_l:<10}{GAME_TITLE:^49}{simbol_r:>10}')
        print('=' * 69)
        # SUBTITLES:
        simbol = '|'
        carrier = 'Porta-Aviões'
        n_carrier = ('5' + ' ' * 2) * 5
        print(f'{n_carrier:>34}{simbol}  {carrier}')
        battleship = 'Battleship'
        n_battleship = ('4' + ' ' * 2) * 4
        print(f'{n_battleship:>34}{simbol}  {battleship}')
        submarine = 'Submarino'
        n_submarine = ('3' + ' ' * 2) * 3
        print(f'{n_submarine:>34}{simbol}  {submarine}')
        destroyer = 'Destroyer'
        n_destroyer = ('2' + ' ' * 2) * 2
        print(f'{n_destroyer:>34}{simbol}  {destroyer}')
        motorboat = 'Lancha'
        n_motorboat = '1' + ' ' * 2
        print(f'{n_motorboat:>34}{simbol}  {motorboat}')
        print('=' * 69)

    def render_intro(self) -> None:
        '''Render intro and get player name.'''
        # TITLE AND DESCRIPTION:
        self.render_title()
        print(GAME_DESCRIPTION)
        print('=' * 69)
        # PLAYER NAME:
        self.player.name = input('\033[34mNOME DO JOGADOR: \033[30;44m')
        print('\033[m')

    def render_map_generator(self) -> None:
        '''Render player map generation.'''
        error = ''
        is_selected = False
        while not is_selected:
            # MAP AND OPTIONS:
            self.render_title()
            self.player.ships_map.render()
            print(self.text_color + '=' * 69)
            print(' 1 - Iniciar jogo')
            print(' 2 - Reposicionar navios')
            print(' 3 - Sair do jogo')
            print('=' * 69)
            # RENDER ERROR:
            if error != '':
                error = self.error_color + 'ERRO: ' + error
                print(f'{error:^69}')
                print(self.text_color + '=' * 69)
            # VERIFY OPTION:
            option = input('\033[34mDIGITE O NUMERO DA OPÇÃO: \033[30;44m')
            print('\033[m')
            option = option.replace(' ', '')
            if option == '1':
                is_selected = True
                error = ''
            elif option == '2':
                self.player.ships_map.table = self.player.ships_map.create_table()
                self.player.ships_map.generate_ships()
                error = ''
            elif option == '3':
                self.is_running = False
            else:
                error = 'Digite apenas o numero da opção escolhida.'

    def render_maps(self) -> None:
        '''Render maps.'''
        for i, line in enumerate(self.player.ships_map.table):
            print(''.join(line) + self.text_color + '|' + (' ' * 2) + ''.join(self.player.hits_map.table[i]))

    def run(self) -> None:
        '''Run game.'''
        self.is_running = True
        # CREATE PLAYER:
        self.player = Player()
        self.player.hits_map = Field()
        self.player.ships_map = Field()
        self.player.ships_map.generate_ships()
        # INTRO:
        self.render_intro()
        # MAP GENERATOR:
        self.render_map_generator()
        # CREATE BOT:
        self.bot = Player(name = 'Bot', is_bot = True)
        self.bot.hits_map = Field()
        self.bot.ships_map = Field()
        self.bot.ships_map.generate_ships()
        # CREATE SCORE BOARD:
        self.score = Score(player_name = self.player.name, bot_name = self.bot.name)
        # START MATCH:
        error = ''
        while self.is_running:
            # RENDER:
            self.render_title()
            self.render_maps()
            self.score.render()
            # RENDER ERROR:
            if error != '':
                error = self.error_color + 'ERRO: ' + error
                print(f'{error:^69}')
            # SHOT:
            shot = input('\033[34mDIGITE O ALVO DO DISPARO: \033[30;44m')
            print('\033[m')
            shot = shot.upper()
            shot = shot.replace(' ', '')
            if shot[0] in self.player.hits_map.lines and shot[1] in self.player.hits_map.columns:
                shot = shot[1] + shot[0]
            if shot[0] in self.player.hits_map.columns and shot[1] in self.player.hits_map.lines:
                print(shot)
                self.is_running = False
            else:
                error = 'Responda apenas com uma letra e um numero.'
            # Realizar disparo.
            # Verificar vitória ou derrota.
            # Variar entre turno do player e do bot.
            # Tela de vitória.
            # Tela de derrota (pegar som de derrota).
            # Continuar ou não.

        # Adicionar efeitos sonoros.
        # Adicionar trilha sonora (função asinc).

        # RESET COLORS:
        print('\033[m')

seabattle = Game()
seabattle.run()
