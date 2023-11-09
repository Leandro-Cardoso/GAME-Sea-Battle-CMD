from random import choice

from config import COLOR_TEXT, COLOR_WATER, COLOR_SHIP, COLOR_FAIL

class Field():
    '''Create game field.'''
    def __init__(self, col_space:int = 2) -> None:
        self.col_space = col_space
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.bg_char = COLOR_WATER + '-'
        self.bg_char_water = COLOR_FAIL + 'X'
        self.ships = {
            'carrier' : 5,
            'battleship' : 4,
            'submarine' : 3,
            'destroyer' : 2,
            'motorboat' : 1
        }
        self.table = self.create_table()

    def get_target_index(self, target:str) -> list:
        '''Get shot index list.'''
        i_column = self.columns.index(target[0]) + 1
        if len(target) == 2:
            i_line = self.lines.index(target[1]) + 1
        else:
            i_line = self.lines.index(target[1] + target[2]) + 1
        return [i_column, i_line]

    def replace_target(self, target:str, target_content:str) -> None:
        '''Replace target content.'''
        # GET INDEX:
        index_list = self.get_target_index(target)
        i_column = index_list[0]
        i_line = index_list[1]
        # REPLACE:
        self.table[i_column][i_line] = target_content

    def create_target_content(self, target:str) -> str:
        '''Create target content to replace.'''
        # GET INDEX:
        index_list = self.get_target_index(target)
        i_column = index_list[0]
        i_line = index_list[1]
        # IS WATER:
        if self.bg_char in self.table[i_column][i_line]:
            return COLOR_FAIL + self.bg_char_water + ' ' * self.col_space
        # IS SHIP:
        else:
            for ship_name in list(self.ships):
                if COLOR_SHIP + str(self.ships[ship_name]) in self.table[i_column][i_line]:
                    return COLOR_FAIL + str(self.ships[ship_name]) + ' ' * self.col_space

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
                    replace = COLOR_SHIP + str(self.ships[ship_name]) + ' ' * self.col_space
                    if orientation == 'vertical':
                        self.table[i_line + j][i_column] = replace
                    else:
                        self.table[i_line][i_column + j] = replace

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
                    line.append(COLOR_TEXT + self.columns[c - 1] + ' ' * self.col_space)
                # NUMBERS:
                elif l != 0 and c == 0:
                    if l == 10:
                        line.append(COLOR_TEXT + self.lines[l - 1] + ' ' * self.col_space)
                    else:
                        line.append(COLOR_TEXT + self.lines[l - 1] + ' ' * (1 + self.col_space))
                # FIELD:
                else:
                    line.append(self.bg_char + ' ' * self.col_space)
            table.append(line)
        return table

    def render(self) -> None:
        '''Render field.'''
        for line in self.table:
            print(''.join(line))
