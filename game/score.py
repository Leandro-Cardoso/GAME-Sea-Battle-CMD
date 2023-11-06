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
        self.text_color = '\033[33m'

    def change_turn(self) -> None:
        '''Change turn.'''
        if self.turn == self.player_name:
            self.turn = self.bot_name
        else:
            self.turn = self.player_name

    def hit(self, target:str = 'Bot') -> None:
        '''Ship hit.'''
        hit = 100 / self.total_hits
        if target == self.player_name:
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
        print(self.text_color + '=' * 32)
        turn = f'É a vez de {self.turn}...'
        print(f'{turn:^32}')
        print(self.text_color + '=' * 32)
        player_name = f'Nome: {self.player_name}'
        print(f'{player_name:<15} | Nome: {self.bot_name}')
        player_life = f'Vida: {int(self.player_life)} %'
        print(f'{player_life:<15} | Vida: {int(self.bot_life)} %')
        player_score = f'Pontos: {self.player_score}'
        print(f'{player_score:<15} | Pontos: {self.bot_score}')
        print('=' * 32)
