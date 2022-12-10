
def randomNim() -> Callable:
    def pure_random(state: Nim) -> Nimply:
        '''Random row, random number of elements'''
        row = random.choice([r for r, c in enumerate(state.rows) if c > 0])
        num_objects = random.randint(1, state.rows[row])
        return Nimply(row, num_objects)
    return pure_random

def gabrieleNim() -> Callable:
    def gabriele(state: Nim) -> Nimply:
        '''Pick always the maximum possible number of the lowest row'''
        possible_moves = [(r, o) for r, c in enumerate(state.rows) for o in range(1, c + 1)]
        return Nimply(*max(possible_moves, key=lambda m: (-m[0], m[1])))
    return gabriele

def optimalStrategy() -> Callable:
    def optimal_strategy(state: Nim) -> Nimply:
        data = cook_status(state)
        return next((bf for bf in data["brute_force"] if bf[1] == 0), random.choice(data["brute_force"]))[0]
    return optimal_strategy

def randomAllNim() -> Callable:
    def randomAll(state: Nim) -> Nimply:
        '''Random row, but pick the maximum number of elements'''
        row = random.choice([r for r, c in enumerate(state.rows) if c > 0])
        num_objects = random.randint(1, state.rows[row])
        return Nimply(row, num_objects)
    return randomAll

def longestAllNim() -> Callable:
    def longestAll(state: Nim) -> Nimply:
        '''Pick always the longest row'''
        row =max((x for x in enumerate(state.rows)), key=lambda y: y[1])[0]
        num_objects = state.rows[row]
        return Nimply(row, num_objects)
    return longestAll

def randomSmartNim() -> Callable: 
    def randomSmart(state: Nim) -> Nimply:
        '''Here the strategy improves on the pure random, where it improves the last move'''
        data = cook_status(state)
        if data["active_rows_number"]==1:
           return Nimply(data["random"], state.rows[data["random"]])
        else: 
            row = random.choice([r for r, c in enumerate(state.rows) if c > 0])
            num_objects = random.randint(1, state.rows[row])
            return Nimply(row, num_objects)
    return randomSmart