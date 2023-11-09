from os import system
from random import choice

from field import Field
from score import Score
from player import Player

from config import GAME_TITLE, GAME_DESCRIPTION, GAME_SFX_PATH
from config import COLOR_TEXT, COLOR_WATER, COLOR_INPUT, COLOR_RESET, COLOR_FAIL, COLOR_SUCCESS

class Game():
    '''Create game file.'''
    def __init__(self) -> None:
        self.is_running = False
        self.player = Player()
        self.bot = Player(name = 'Bot', is_bot = True)
        self.score = Score()

    def render_title(self) -> None:
        '''Render title and subtitles.'''
        # RESET SCREEN:
        system('cls')
        # TITLE:
        print(COLOR_TEXT + '=' * 69)
        n_simbols = 3
        simbol_l = '>' * n_simbols
        simbol_r = '<' * n_simbols
        print(f'{simbol_l:<10}{GAME_TITLE:^49}{simbol_r:>10}')
        print('=' * 69)

    def render_subtitles(self) -> None:
        '''Render subtitles.'''
        simbol = '|'
        carrier = '1x Porta-Aviões'
        n_carrier = ('5' + ' ' * 2) * 5
        print(f'{n_carrier:>34}{simbol}  {carrier}')
        battleship = '2x Battleship'
        n_battleship = ('4' + ' ' * 2) * 4
        print(f'{n_battleship:>34}{simbol}  {battleship}')
        submarine = '3x Submarino'
        n_submarine = ('3' + ' ' * 2) * 3
        print(f'{n_submarine:>34}{simbol}  {submarine}')
        destroyer = '4x Destroyer'
        n_destroyer = ('2' + ' ' * 2) * 2
        print(f'{n_destroyer:>34}{simbol}  {destroyer}')
        motorboat = '5x Lancha'
        n_motorboat = '1' + ' ' * 2
        print(f'{n_motorboat:>34}{simbol}  {motorboat}')
        print('=' * 69)

    def render_intro(self) -> None:
        '''Render intro and get player name.'''
        # TITLE AND DESCRIPTION:
        self.render_title()
        self.render_subtitles()
        print(GAME_DESCRIPTION)
        print('=' * 69)
        # PLAYER NAME:
        self.player.name = input(COLOR_WATER + 'NOME DO JOGADOR: ' + COLOR_INPUT)
        print(COLOR_RESET)

    def render_map_generator(self) -> None:
        '''Render player map generation.'''
        error = ''
        is_selected = False
        while not is_selected:
            # MAP AND OPTIONS:
            self.render_title()
            self.render_subtitles()
            self.player.ships_map.render()
            print(COLOR_TEXT + '=' * 69)
            print(' 1 - Iniciar jogo')
            print(' 2 - Reposicionar navios')
            print(' 3 - Sair do jogo')
            print('=' * 69)
            # RENDER ERROR:
            if error != '':
                error = COLOR_FAIL + 'ERRO: ' + error
                print(f'{error:^69}')
                error = ''
                print(COLOR_TEXT + '=' * 69)
            # VERIFY OPTION:
            option = input(COLOR_WATER + 'DIGITE O NUMERO DA OPÇÃO: ' + COLOR_INPUT)
            print(COLOR_RESET)
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
                is_selected = True
                error = ''
            else:
                error = 'Digite apenas o numero da opção escolhida.'

    def render_maps(self) -> None:
        '''Render maps.'''
        for i, line in enumerate(self.player.ships_map.table):
            print(''.join(line) + COLOR_TEXT + '|' + (' ' * 2) + ''.join(self.player.hits_map.table[i]))

    def new_game(self) -> None:
        '''New game.'''
        # RESET SCORE BOARD:
        self.score.player_life = 100
        self.score.bot_life = 100
        self.score.turn = self.score.player_name
        # RESET PLAYER FIELD:
        self.player.hits_map = Field()
        self.player.ships_map = Field()
        self.player.ships_map.generate_ships()
        # RESET BOT FIELD:
        self.bot.hits_map = Field()
        self.bot.ships_map = Field()
        self.bot.ships_map.generate_ships()

    def render_victory(self) -> None:
        '''Render victory.'''
        error = ''
        is_selected = False
        while not is_selected:
            # RENDER TITLE:
            self.render_title()
            # RENDER VICTORY MSG:
            msg = f'{self.player.name} venceu !!!'
            print(f'{COLOR_SUCCESS}{msg:^69}')
            msg = 'Parabéns !!!'
            print(f'{msg:^69}')
            # RENDER SCORE:
            self.score.render()
            # RENDER OPTIONS:
            print(' 1 - Continuar jogando')
            print(' 2 - Sair do jogo')
            print('=' * 69)
            # RENDER ERROR:
            if error != '':
                error = COLOR_FAIL + 'ERRO: ' + error
                print(f'{error:^69}')
                error = ''
                print(COLOR_TEXT + '=' * 69)
            # VERIFY OPTION:
            option = input(COLOR_WATER + 'DIGITE O NUMERO DA OPÇÃO: ' + COLOR_INPUT)
            print(COLOR_RESET)
            option = option.replace(' ', '')
            if option == '1':
                self.new_game()
                is_selected = True
                error = ''
            elif option == '2':
                self.is_running = False
                is_selected = True
                error = ''
            else:
                error = 'Digite apenas o numero da opção escolhida.'

    def render_defeat(self) -> None:
        '''Render defeat.'''
        error = ''
        is_selected = False
        while not is_selected:
            # RENDER TITLE:
            self.render_title()
            # RENDER DEFEAT MSG:
            msg = f'{self.player.name} perdeu !!!'
            print(f'{COLOR_FAIL}{msg:^69}')
            msg = 'Tente novamente ...'
            print(f'{msg:^69}')
            # RENDER SCORE:
            self.score.render()
            # RENDER OPTIONS:
            print(' 1 - Continuar jogando')
            print(' 2 - Sair do jogo')
            print('=' * 69)
            # RENDER ERROR:
            if error != '':
                error = COLOR_FAIL + 'ERRO: ' + error
                print(f'{error:^69}')
                error = ''
                print(COLOR_TEXT + '=' * 69)
            # VERIFY OPTION:
            option = input(COLOR_WATER + 'DIGITE O NUMERO DA OPÇÃO: ' + COLOR_INPUT)
            print(COLOR_RESET)
            option = option.replace(' ', '')
            if option == '1':
                self.new_game()
                is_selected = True
                error = ''
            elif option == '2':
                self.is_running = False
                is_selected = True
                error = ''
            else:
                error = 'Digite apenas o numero da opção escolhida.'

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
        player_feedback = ''
        bot_feedback = ''
        error = ''
        while self.is_running:
            # RENDER:
            self.render_title()
            self.render_subtitles()
            self.render_maps()
            self.score.render()
            # PLAYER TURN:
            if self.score.turn == self.player.name:
                # RENDER FEEDBACK:
                if player_feedback != '' or bot_feedback != '':
                    print(f'{player_feedback:^69}')
                    print(f'{bot_feedback:^69}')
                    print(COLOR_TEXT + '=' * 69)
                    player_feedback = ''
                    bot_feedback = ''
                # RENDER ERROR:
                if error != '':
                    error = COLOR_FAIL + 'ERRO: ' + error
                    print(f'{error:^69}')
                    error = ''
                # VALIDATE SHOT:
                shot = input(COLOR_WATER + 'DIGITE O ALVO DO DISPARO: ' + COLOR_INPUT)
                print(COLOR_RESET)
                shot = shot.upper()
                shot = shot.replace(' ', '')
                if shot[0] in self.player.hits_map.lines and not len(shot) == 1:
                    if len(shot) == 3 and shot[0] + shot[1] == '10':
                        shot = shot[2] + shot[0] + shot[1]
                    else:
                        shot = shot[1] + shot[0]
                if len(shot) == 1:
                    error = 'Responda apenas com uma letra e um numero.'
                elif shot[0] in self.player.hits_map.columns and shot[1] in self.player.hits_map.lines and len(shot) == 2 or len(shot) == 3 and shot[1] + shot[2] == '10':
                    # SHOT:
                    target_content = self.bot.ships_map.create_target_content(shot)
                    self.player.hits_map.replace_target(shot, target_content)
                    if self.bot.ships_map.bg_char_water not in target_content:
                        if shot not in self.player.shots:
                            self.score.hit(self.bot.name)
                        # FEEDBACK:
                        player_feedback = f'{COLOR_SUCCESS}{self.player.name}: {shot} - Acertou um navio !!!'
                    else:
                        player_feedback = f'{COLOR_TEXT}{self.player.name}: {shot} - Errou o alvo !!!'
                    # ADD TO SHOTS LIST:
                    if shot not in self.player.shots:
                        self.player.shots.append(shot)
                elif shot == '0':
                    self.is_running = False
                else:
                    error = 'Responda apenas com uma letra e um numero.'
            # BOT TURN:
            else:
                # VALIDATE SHOT:
                is_valid_shot = False
                while not is_valid_shot:
                    column = choice(self.bot.hits_map.columns)
                    line = choice(self.bot.hits_map.lines)
                    shot = column + line
                    if shot not in self.bot.shots:
                        is_valid_shot = True
                # SHOT:
                target_content = self.player.ships_map.create_target_content(shot)
                self.bot.hits_map.replace_target(shot, target_content)
                self.player.ships_map.replace_target(shot, target_content)
                if self.player.ships_map.bg_char_water not in target_content:
                    if shot not in self.bot.shots:
                        self.score.hit(self.player.name)
                    # FEEDBACK:
                    bot_feedback = f'{COLOR_FAIL}{self.bot.name}: {shot} - Acertou um navio !!!'
                else:
                    bot_feedback = f'{COLOR_TEXT}{self.bot.name}: {shot} - Errou o alvo !!!'
                # ADD TO SHOTS LIST:
                self.bot.shots.append(shot)
            # CHANGE TURN:
            if error == '':
                self.score.change_turn()
            # VICTORY:
            if self.score.bot_life == 0:
                self.render_victory()
            # DEFEAT:
            elif self.score.player_life == 0:
                self.render_defeat()

        # Pegar som de derrota.
        # Adicionar efeitos sonoros.
        # Adicionar trilha sonora (função asinc).
        # Criar executável.
        # Finalizar README.

        # RESET COLORS:
        print(COLOR_RESET)

seabattle = Game()
seabattle.run()
