from Node import Node
from Problem import Problem
from queue import PriorityQueue

# Uniform Cost Search
def uniform_cost_search(problem):
    nodes = PriorityQueue()
    nodes.put((0, Node(problem.initial_state))) 
    while not nodes.empty():
        _, node = nodes.get()
        if problem.goal_test(node.state):
            return node 
        for child in problem.expand(node):
            nodes.put((child.path_cost, child))
    return "failure"  

# A* Misplaced Tile Heuristic
def misplaced_tile_heuristic(state, goal_state):
    return sum(s != g for row_s, row_g in zip(state, goal_state) for s, g in zip(row_s, row_g))
    
def astar_misplaced_tile(problem):
    nodes = PriorityQueue()
    nodes.put((0, Node(problem.initial_state)))  
    while not nodes.empty():
        _, node = nodes.get()
        if problem.goal_test(node.state):
            return node  
        for child in problem.expand(node):
            heuristic_cost = misplaced_tile_heuristic(child.state, problem.goal_state)
            total_cost = child.path_cost + heuristic_cost
            nodes.put((total_cost, child))
    return "failure" 

# A* Euclidean Distance Heuristic
def euclidean_distance_heuristic(state, goal_state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_i, goal_j = next((x, y) for x in range(3) for y in range(3) if goal_state[x][y] == state[i][j])
                distance += math.sqrt((goal_i - i)**2 + (goal_j - j)**2)
    return distance

def astar_euclidean_distance(problem):
    nodes = PriorityQueue()
    nodes.put((0, Node(problem.initial_state)))  
    while not nodes.empty():
        _, node = nodes.get()
        if problem.goal_test(node.state):
            return node 
        for child in problem.expand(node):
            heuristic_cost = euclidean_distance_heuristic(child.state, problem.goal_state)
            total_cost = child.path_cost + heuristic_cost
            nodes.put((total_cost, child))
    return "failure"  



def main():
    print("Welcome to dcoel003, abrem005, jgonz671, 8 puzzle solver.")

    initalState = [[1,2,3],[4,8,0],[7,6,5]]
    goalState = [[1,2,3],[4,5,6],[7,8,0]]
    operators = ['up', 'down', 'left', 'right']
    problem = Problem(initalState, goalState, operators)
    print(initalState[0], '\n', initalState[1], '\n', initalState[2])

    solutionNode = uniform_cost_search(problem)
    solutionNode2= astar_misplaced_tile(problem)
    solutionNode3 = astar_euclidean_distance(problem)

    if ((solutionNode and solutionNode2 and solutionNode3) != "failure"):
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