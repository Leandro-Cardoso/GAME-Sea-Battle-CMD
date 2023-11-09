from config import COLOR_TEXT

class Score():
    '''Create score board.'''
    def __init__(self, player_name:str = 'Player', bot_name:str = 'Bot') -> None:
        self.total_hits = 35 # (1 * 5) + (2 * 4) + (3 * 3) + (4 * 2) + (5 * 1)
        self.player_name = player_name
        self.bot_name = bot_name
        self.player_life = 100
        self.bot_life = 100
        self.player_score = 0
        self.bot_score = 0
        self.turn = self.player_name

    def change_turn(self) -> None:
        '''Change turn.'''
        if self.turn == self.player_name:
            self.turn = self.bot_name
        else:
            self.turn = self.player_name

    def hit(self, target_name:str = 'Bot') -> None:
        '''Ship hit.'''
        hit = 100 / self.total_hits
        if target_name == self.player_name:
            self.player_life -= hit
            if self.player_life <= 0:
                self.player_life = 0
                self.bot_score += 1
        else:
            self.bot_life -= hit
            if self.bot_life <= 0:
                self.bot_life = 0
                self.player_score += 1

    def reset(self) -> None:
        '''Reset scores.'''
        self.player_life = 100
        self.bot_life = 100
        self.player_score = 0
        self.bot_score = 0
        self.turn = self.player_name

    def render(self) -> None:
        '''Render score board.'''
        # SCORES:
        print(COLOR_TEXT + '=' * 69)
        player_name = f'Nome: {self.player_name}'
        print(f'{player_name:<33} | Nome: {self.bot_name}')
        player_life = f'Vida: {int(self.player_life)} %'
        print(f'{player_life:<33} | Vida: {int(self.bot_life)} %')
        player_score = f'Pontos: {self.player_score}'
        print(f'{player_score:<33} | Pontos: {self.bot_score}')
        print('=' * 69)
        # TURN:
        turn = f'É a vez de {self.turn}...'
        print(f'{turn:^69}')
        print('=' * 69)
