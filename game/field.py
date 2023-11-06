class Field():
    '''Create game field.'''
    def __init__(self, col_space:int = 2) -> None:
        self.col_space = col_space
        self.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.lines = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.bg_char = '+'
        self.bg_color = '\033[34m'
        self.text_color = '\033[33m'
        self.table = self.create_table()

    def generate_ships(self) -> None:
        '''Generate ships'''
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
