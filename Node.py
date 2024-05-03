class Node:
    def __init__(self, state, parent=None, action=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic

    def get_state(self):
        return self.state 

    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action

    def get_heuristic(self):
        return self.heuristic

    def set_state(self, state):
        self.state = state

    def set_parent(self, parent):
        self.parent = parent

    def set_action(self, action):
        self.action = action

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic