from Node import Node
from Problem import Problem
from queue import PriorityQueue

# Uniform Cost Search
def uniform_cost_search(problem):
    nodes = PriorityQueue()
    nodes.put((0, Node(problem.initial_state)))  # (priority, node)
    while not nodes.empty():
        _, node = nodes.get()
        if problem.goal_test(node.state):
            return node  # Solution found
        for child in problem.expand(node):
            nodes.put((child.path_cost, child))
    return "failure"  # No solution found

# A* Misplaced Tile Heuristic
def misplaced_tile_heuristic(state, goal_state):
    return 
    
def astar_misplaced_tile(problem):
    return 

# A* Euclidean Distance Heuristic
def euclidean_distance_heuristic(state, goal_state):
    return 

def astar_euclidean_distance(problem):
    return 



def main():
    print("Welcome to dcoel003, abrem005, jgonz671, 8 puzzle solver.")

    initalState = [[1,2,3],[4,8,0],[7,6,5]]
    goalState = [[1,2,3],[4,5,6],[7,8,0]]
    operators = ['up', 'down', 'left', 'right']
    problem = Problem(initalState, goalState, operators)
    print(initalState[0], '\n', initalState[1], '\n', initalState[2])

    solutionNode = uniform_cost_search(problem)

    if (solutionNode != "failure"):
        print("solution node isn't a failure")

        # Print the path from the initial state to the goal state
        path = []
        while solution_node:
            path.append(solution_node.state)
            solution_node = solution_node.parent
        path.reverse()
        for state in path:
            print(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()