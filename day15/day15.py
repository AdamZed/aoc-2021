import heapq

def children(goal, node):
    X, Y = goal
    x, y = node
    if x > 0: yield (x-1, y)
    if x < X: yield (x+1, y)
    if y > 0: yield (x, y-1)
    if y < Y: yield (x, y+1)

def cost_of(data, x, y):
    X, Y = len(data), len(data[0])
    i, _x = divmod(x, X)
    j, _y = divmod(y, Y)
    cost = data[_x][_y] + i + j
    while cost > 9: cost = cost - 9
    return cost

def ucs_cost(data, GOAL):
    bestcosts = {}
    q = [(0, (0, 0))]
    while len(q) > 0:
        cost, node = heapq.heappop(q)
        x, y = node
        if (x, y) == GOAL: return cost
        for _node in children(GOAL, node):
            (x1, y1) = _node
            _cost = cost + cost_of(data, x1, y1)
            if _node in bestcosts and bestcosts[_node] <= _cost: continue
            bestcosts[_node] = _cost
            heapq.heappush(q, (_cost, _node))

def part1(data):
    GOAL = (len(data)-1, len(data[0])-1)
    return ucs_cost(data, GOAL) 

def part2(data):
    GOAL = (len(data)*5-1, len(data[0])*5-1)
    return ucs_cost(data, GOAL) 

def main(fname):
    with open(fname) as f:
        data = [[int(x) for x in row.strip()] for row in f.read().strip().split("\n")]

    print(f'Part 1: {part1(data)}')
    print(f'Part 2: {part2(data)}')

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    main(filename)