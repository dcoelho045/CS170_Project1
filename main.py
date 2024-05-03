# from Node import Node
# from Problem import Problem
# from queue import PriorityQueue

# # Uniform Cost Search --------------------- Does not work
# def uniform_cost_search(problem):
#     nodes = PriorityQueue()
#     nodes.put((0, Node(problem.initial_state)))  # (priority, node)
#     while not nodes.empty():
#         _, node = nodes.get()
#         if problem.goal_test(node.state):
#             return node  # Solution found
#         for child in problem.expand(node):
#             nodes.put((child.path_cost, child))
#     return "failure"  # No solution found

# # A* Misplaced Tile Heuristic
# def misplaced_tile_heuristic(state, goal_state):
#     misplaced_tiles = 0
#     for i in range(3):
#         for j in range(3):
#             if state[i][j] != goal_state[i][j]:
#                 misplaced_tiles += 1
#     return misplaced_tiles
    
# def astar_misplaced_tile(problem):
#     nodes = PriorityQueue()
#     initial_node = Node(problem.initial_state, heuristic=misplaced_tile_heuristic(problem.initial_state, problem.goal_state))
#     nodes.put((initial_node.heuristic, initial_node))  # (priority, node)
#     while not nodes.empty():
#         _, node = nodes.get()
#         if problem.goal_test(node.state):
#             return node  # Solution found
#         for child in node.expand():
#             child_node = Node(child, node, heuristic=misplaced_tile_heuristic(child, problem.goal_state))
#             nodes.put((child_node.heuristic + child_node.path_cost, child_node))
#     return "failure"  # No solution found

# # A* Euclidean Distance Heuristic
# def euclidean_distance_heuristic(state, goal_state):
#     return 

# def astar_euclidean_distance(problem):
#     return 

def main():
    print("Welcome to dcoel003, abrem005, jgonz671, 8 puzzle solver.")
    response = input("Type “1” to use a default puzzle, or “2” to enter your own puzzle. \n")
    
    if (response == '2'):
        input1 = [int(x) for x in input("Enter the first row: ").split()]
        input2 = [int(x) for x in input("Enter the second row: ").split()]
        input3 = [int(x) for x in input("Enter the third row: ").split()]

        intial_state = [input1, input2, input3]

        print(intial_state[0])
        print(intial_state[1])
        print(intial_state[2])

    # initial_state = [[1,2,3],[4,8,0],[7,6,5]]
    # goal_state = [[1,2,3],[4,5,6],[7,8,0]]
    # operators = ['up', 'down', 'left', 'right']
    # problem = Problem(initial_state, goal_state, operators)
    # print(initial_state[0], '\n', initial_state[1], '\n', initial_state[2])

    # solution_node = astar_misplaced_tile(problem)

if __name__ == "__main__":
    main()