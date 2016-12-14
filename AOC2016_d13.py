import itertools
import copy
fav_number = 1364

INF_COST = 9999

def get_element((x, y), fv=fav_number):
    val = str(bin((x*x + 3*x + 2*x*y + y + y*y) + fv))
    num_1 = len(filter(lambda x: x == '1', [c for c in val]))
    output = ''
    if num_1 % 2: 
        output = '#' 
    else: output = '.'
    return output

def get_maze(max_dim):
    l = [c for c in xrange(max_dim)]
    coordinates = [c for c in itertools.product(l, repeat=2)] 
    elements = map(get_element, coordinates)
    return elements

def print_maze(elements, max_dim):
    s = ''
    for x in xrange(max_dim):
        for y in xrange(max_dim):
            s += elements[y*max_dim + x] + ' '
        s += '\n'
    print(s)

def cost_elem(elements, coord, max_dim):
    if ((coord[0] >= max_dim) or 
        (coord[1] >= max_dim) or 
        (coord[0] < 0) or
        (coord[1] < 0)):
            return INF_COST
    if elements[coord[0]*max_dim + coord[1]] == '.':
        return 1
    else:
        return INF_COST

def solve_maze(pos_storage, elements, max_dim, start_pos, end_pos):
    cost = 0
    mincost = INF_COST
    if cost_elem(elements, end_pos, max_dim) < INF_COST:
        elements[end_pos[0]*max_dim+ end_pos[1]] = 'O'
    else:
        return INF_COST, elements

    if start_pos == end_pos:
        cost = 0
    elif end_pos in pos_storage:
        cost = pos_storage[end_pos]
    else:
        up = (end_pos[0], end_pos[1]-1)
        down = (end_pos[0], end_pos[1]+1)
        left = (end_pos[0]-1, end_pos[1])
        right = (end_pos[0]+1, end_pos[1])
        pos_moves = filter(lambda x: cost_elem(elements, x, max_dim) < INF_COST, 
                            [up, down, left,right])
        costs = []
        for move in pos_moves:
            costs.append(solve_maze(pos_storage, elements, max_dim, start_pos,
                move)[0] + cost_elem(elements, move, max_dim))
        print('from {0} to {1} = {2}'.format(start_pos, end_pos, costs))
        if len(costs):
            cost = min(costs)
            pos_storage[end_pos] = cost
        else:
            elements[end_pos[0]*max_dim +end_pos[1]] = 'X'
        if cost < mincost: 
            mincost = cost
    return mincost, elements

pos_storage = {}
cost, elements = solve_maze(pos_storage, get_maze(50), 50, (1,1), (31,39))
print_maze(elements, 50)
print(cost)

