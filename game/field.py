from random import choice

class Field():
    '''Create game field.'''
    def __init__(self, col_space:int = 2) -> None:
        self.col_space = col_space
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.bg_char = '+'
        self.ships = {
            'carrier' : 5,
            'battleship' : 4,
            'submarine' : 3,
            'destroyer' : 2,
            'motorboat' : 1
        }
        self.bg_color = '\033[34m'
        self.text_color = '\033[33m'
        self.ship_color = '\033[37m'
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
        for i, ship_name in enumerate(self.ships):
            size = self.ships[ship_name]
            # SHIP NUMBER:
            n_ship = i + 1
            for n in range(n_ship):
                # VERIFY SET POSITION:
                is_set_ship_position = False
                while not is_set_ship_position:
                    column = choice(self.columns)
                    line = choice(self.lines)
                    orientation = choice(['vertical', 'horizontal'])
                    i_column = self.columns.index(column) + 1
                    i_line = self.lines.index(line) + 1
                    is_set_ship_position = True
                    for j in range(size):
                        try:
                            if orientation == 'vertical':
                                if self.bg_char not in str(self.table[i_line + j][i_column]):
                                    is_set_ship_position = False
                            else:
                                if self.bg_char not in str(self.table[i_line][i_column + j]):
                                    is_set_ship_position = False
                        except:
                            is_set_ship_position = False
                # SET POSITION:
                for j in range(size):
                    replace = self.ship_color + str(self.ships[ship_name])
                    if orientation == 'vertical':
                        self.table[i_line + j][i_column] = str(self.table[i_line + j][i_column]).replace(self.bg_char, replace)
                    else:
                        self.table[i_line][i_column + j] = str(self.table[i_line][i_column + j]).replace(self.bg_char, replace)

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
