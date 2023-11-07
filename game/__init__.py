from os import system

from field import Field
from score import Score
from player import Player

from config import GAME_TITLE, GAME_DESCRIPTION

class Game():
    '''Create game file.'''
    def __init__(self) -> None:
        self.is_running = False
        self.command = None
        self.quit_game_commands = ['quit', 'sair', '0']
        self.player = Player()
        self.bot = Player(name = 'Bot', is_bot = True)
        self.score = Score()
        self.text_color = '\033[33m'
        self.error_color = '\033[31m'
        self.success_color = '\033[32m'

    def render_title(self) -> None:
        '''Render title and subtitles.'''
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
        self.render_title()
        print(GAME_DESCRIPTION)
        print('=' * 69)
        self.player.name = input('\033[34mNOME DO JOGADOR: \033[30;44m')
        print('\033[m')

    def render_map_generation(self) -> None:
        '''Render player map generation.'''
        pass

    def render_maps(self) -> None:
        '''Render maps.'''
        for i, line in enumerate(self.player.ships_map.table):
            print(''.join(line) + self.text_color + '|' + (' ' * 2) + ''.join(self.player.hits_map.table[i]))

    def quit(self) -> None:
        '''Quit game.'''
        self.is_running = False

    def start(self) -> None:
        '''Start game.'''
        # CREATE PLAYER:
        self.player = Player()
        self.player.hits_map = Field()
        self.player.ships_map = Field()
        self.player.ships_map.generate_ships()
        # INTRO:
        self.render_intro()
        system('cls')

        # CREATE BOT:
        self.bot = Player(name = 'Bot', is_bot = True)
        self.bot.hits_map = Field()
        self.bot.ships_map = Field()
        self.bot.ships_map.generate_ships()

        # CREATE SCORE BOARD:
        self.score = Score(player_name = self.player.name, bot_name = self.bot.name)

        # TESTS: (temp)
        self.render_title()
        self.render_maps()
        self.score.render()
        self.is_running = False

    def update(self) -> None:
        '''While game is running.'''
        while self.is_running:
            # CLEAR CMD:
            system('cls')

            # QUIT GAME:
            if str(self.command).lower() in self.quit_game_commands:
                self.is_running = False
    
    def run(self) -> None:
        '''Run game.'''
        self.is_running = True
        self.start()
        self.update()
        print('\033[m')

seabattle = Game()
seabattle.run()
