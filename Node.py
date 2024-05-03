class Node:
    def __init__(self, state, parent=None, action=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic