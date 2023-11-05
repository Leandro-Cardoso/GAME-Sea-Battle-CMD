class Score():
    '''Create score board.'''
    def __init__(self, player_name:str = 'Player') -> None:
        self.player_name = player_name
        self.bot_name = 'Bot'
        self.player_life = 100
        self.bot_life = 100
        self.player_score = 0
        self.bot_score = 0
        self.turn = self.player_name

    def render(self) -> None:
        '''Render score board.'''
        pass
