from random import choice

class Field():
    '''Create game field.'''
    def __init__(self, col_space:int = 2) -> None:
        self.col_space = col_space
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.bg_char = '+'
        self.ships = {
            'carrier' : {
                'code' : 'C',
                'size' : 5
            },
            'battleship' : {
                'code' : 'B',
                'size' : 4
            },
            'submarine' : {
                'code' : 'S',
                'size' : 3
            },
            'destroyer' : {
                'code' : 'D',
                'size' : 2
            },
            'motorboat' : {
                'code' : 'M',
                'size' : 1
            }
        }
        self.bg_color = '\033[34m'
        self.text_color = '\033[33m'
        self.ship_color = '\033[30m'
        self.table = self.create_table()

    def is_field(self, position:str) -> bool:
        '''Is field?'''
        pass

    def is_ship(self, position:str) -> bool:
        '''Is ship?'''
        pass

    def generate_ships(self) -> None:
        '''Generate ships'''
        # SHIP TYPE:
        for i in range(list(self.ships)):
            ship = self.ships[i]
            # SHIP NUMBER:
            n_ship = i + 1
            for n in range(n_ship):
                # SET POSITION:
                is_set_ship_position = False
                while not is_set_ship_position:
                    position = choice(self.columns) + choice(self.lines)
                    orientation = choice(['vertical', 'horizontal'])
                    for j in range(ship['size']):
                        # VERIFICAR SE CABE O NAVIO (OPERAÇÕES COM CONDICIONAIS)...
                        pass
                for j in range(ship['size']):
                    # SETAR POSIÇÕES...
                    pass

    def create_table(self) -> list:
        '''Create table.'''
        table = []
        for l in range(0, 11):
            line = []
            for c in range(0, 11):
                if l == 0 and c == 0:
                    line.append(' ' * (2 + self.col_space))
                # LETTERS:
                elif l == 0 and c != 0:
                    line.append(self.text_color + self.columns[c - 1] + ' ' * self.col_space)
                # NUMBERS:
                elif l != 0 and c == 0:
                    if l == 10:
                        line.append(self.text_color + self.lines[l - 1] + ' ' * self.col_space)
                    else:
                        line.append(self.text_color + self.lines[l - 1] + ' ' * (1 + self.col_space))
                # FIELD:
                else:
                    line.append(self.bg_color + self.bg_char + ' ' * self.col_space)
            table.append(line)
        return table

    def render(self) -> None:
        '''Render field.'''
        for line in self.table:
            print(''.join(line))
        print('')
