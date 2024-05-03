class Problem:
    def __init__(self, initial_state, goal_state, operators):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.operators = operators

    def goal_test(self, state):
        return state == self.goal_state    
    def expand(self, node):
        expanded_nodes = []
        directions = {'up': -1, 'down': 1, 'left': -1, 'right': 1}
        x, y = next((i, j) for i in range(3) for j in range(3) if node.state[i][j] == 0)
        for move in self.operators:
            if move in ['up', 'down']:
                new_x = x + directions[move]
                if 0 <= new_x < 3:
                    new_state = [row[:] for row in node.state]
                    new_state[x][y], new_state[new_x][y] = new_state[new_x][y], new_state[x][y]
                    expanded_nodes.append(Node(new_state, node, move, node.path_cost + 1))
            else:
                new_y = y + directions[move]
                if 0 <= new_y < 3:
                    new_state = [row[:] for row in node.state]
                    new_state[x][y], new_state[x][new_y] = new_state[x][new_y], new_state[x][y]
                    expanded_nodes.append(Node(new_state, node, move, node.path_cost + 1))
        return expanded_nodes

