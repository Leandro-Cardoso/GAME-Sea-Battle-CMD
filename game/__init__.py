from os import system

from field import Field
from score import Score
from player import Player

class Game():
    '''Create game file.'''
    def __init__(self) -> None:
        self.is_running = False
        self.command = None
        self.quit_game_commands = ['quit', 'sair', '0']
        self.player = Player()
        self.bot = Player(name = 'Bot', is_bot = True)
        self.score = Score()
        self.error_color = '\033[31m'
        self.success_color = '\033[32m'

    def quit(self) -> None:
        '''Quit game.'''
        self.is_running = False

    def start(self) -> None:
        '''Start game.'''
        # CREATE PLAYER:
        self.player = Player()
        self.player.name = input('Qual o seu nome? ')
        self.player.hits_map = Field()
        self.player.ships_map = Field()

        # CREATE BOT:
        self.bot = Player(name = 'Bot', is_bot = True)
        self.bot.hits_map = Field()
        self.bot.ships_map = Field()

        # CREATE SCORE BOARD:
        self.score = Score(player_name = self.player.name, bot_name = self.bot.name)

        # TESTS: (temp)
        self.player.hits_map.render()
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

#input('\033[34mATIRAR EM: \033[30;44m')
