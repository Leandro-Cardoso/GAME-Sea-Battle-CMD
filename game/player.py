class Player():
    '''Create player.'''
    def __init__(self, name:str = 'Player', is_bot:bool = False) -> None:
        self.name = name
        self.is_bot = is_bot
        self.ships_map = None
        self.hits_map = None
        self.shots = []
    
    def reset_maps(self) -> None:
        '''Reset game maps.'''
        self.ships_map = None
        self.hits_map = None
