from search import *
import time

#################
# Problem class #
#################
#427
class NAmazonsProblem(Problem):
    """The problem of placing N amazons on an NxN state with none attacking
    each other. A state is represented as an N-element array, where
    a value of r in the c-th entry means there is an empress at column c,
    row r, and a value of -1 means that the c-th column has not been
    filled in yet. We fill in columns left to right.
    """
    def __init__(self, N):
        self.N = N
        self.initial = tuple([-1] * N) # positions des amazones

    def actions(self, state):
        possible_actions = []
        if state[-1] != -1:
            return []    
        for i in range(self.N):
            if(self.conflict(self.result(state, i))): 
                possible_actions.append(i)
        return possible_actions

    def result(self, state, row):
        new_state = list(state)  # Convert tuple to list for modification
        c = new_state.count(-1)  # Count the number of empty columns
        new_state[self.N - c] = row  # Place the queen in the next empty column
        return tuple(new_state)
    def conflict(self, state):
        n = len(state)

        # Check for each Amazon in the state
        for i in range(n):
            for j in range(i + 1, n):
                if(state[i] != -1 and state[j] != -1):
                # Check if the current Amazon attacks any other Amazon
                    if (state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]) or abs(i - j) == 3 * abs(state[i] - state[j]) or abs(i - j) == abs(3 * (state[i] - state[j]))) or abs(i - j) == 4 * abs(state[i] - state[j]) or abs(i - j) == abs(4 * (state[i] - state[j])):
                        return False  # If any attack is found, return False
        return True
    
    def goal_test(self, state):
        n = len(state)
        if -1 in state:
            return False

        # Check for each Amazon in the state
        for i in range(n):
        
            for j in range(i + 1, n):
                # Check if the current Amazon attacks any other Amazon
                if (state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]) or abs(i - j) == 3 * abs(state[i] - state[j]) or abs(i - j) == abs(3 * (state[i] - state[j]))) or abs(i - j) == 4 * abs(state[i] - state[j]) or abs(i - j) == abs(4 * (state[i] - state[j])):
                    return False  # If any attack is found, return False
        return True  # If no attack is found, return True

    def h(self, node):
        """Return number of conflicting queens for a given node"""
        num_conflicts = 0
        for i in range(n):
            for j in range(i + 1, n):
                # Check if the current Amazon attacks any other Amazon
                if (abs(i - j) == abs(state[i] - state[j]) or abs(i - j) == 3 * abs(state[i] - state[j]) or abs(i - j) == abs(3 * (state[i] - state[j]))) or abs(i - j) == 4 * abs(state[i] - state[j]) or abs(i - j) == abs(4 * (state[i] - state[j])):
                    num_conflicts += 1  # If any attack is found, +1

        return num_conflicts

#####################
# Launch the search #
#####################

problem = NAmazonsProblem(int(sys.argv[1]))

start_timer = time.perf_counter()

node = breadth_first_graph_search(problem)



end_timer = time.perf_counter()



# example of print
path = node.path()

print('Number of moves: ', str(node.depth))

for n in path:

    print(n.state)  # assuming that the _str_ function of state outputs the correct format

    print()
    
print("Time: ", end_timer - start_timer)