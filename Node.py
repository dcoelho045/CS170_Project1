class Node:
    def __init__(self, state, parent=None, action=None, heuristic=0, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.path_cost = path_cost
        self.blank_row, self.blank_col = self.find_blank_tile()

    def expand(self):
        children = []
        # Try moving the blank tile in all four directions
        for move_func in [self.move_up, self.move_down, self.move_left, self.move_right]:
            child = move_func()
            if child is not None:
                children.append(child)
        return children

    def move_up(self):
        if self.blank_row == 0:
            return None  # Cannot move up
        new_state = self.swap(self.blank_row, self.blank_col, self.blank_row - 1, self.blank_col)
        return Node(new_state, self, 'up', self.heuristic)

    def move_down(self):
        if self.blank_row == 2:
            return None  # Cannot move down
        new_state = self.swap(self.blank_row, self.blank_col, self.blank_row + 1, self.blank_col)
        return Node(new_state, self, 'down', self.heuristic)

    def move_left(self):
        if self.blank_col == 0:
            return None  # Cannot move left
        new_state = self.swap(self.blank_row, self.blank_col, self.blank_row, self.blank_col - 1)
        return Node(new_state, self, 'left', self.heuristic)

    def move_right(self):
        if self.blank_col == 2:
            return None  # Cannot move right
        new_state = self.swap(self.blank_row, self.blank_col, self.blank_row, self.blank_col + 1)
        return Node(new_state, self, 'right', self.heuristic)

    def find_blank_tile(self):
        for i, row in enumerate(self.state):
            for j, value in enumerate(row):
                if value == 0:
                    return i, j

    def swap(self, row1, col1, row2, col2):
        new_state = [list(row) for row in self.state]
        new_state[row1][col1], new_state[row2][col2] = new_state[row2][col2], new_state[row1][col1]
        return new_state