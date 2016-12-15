import itertools
import copy
fav_number = 1364

INF_COST = 9999
max_level = 100

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
    if elements[coord[0]*max_dim + coord[1]] == '#':
        return INF_COST
    else:
        return 1

def solve_maze(ps, visited, elements, max_dim, start_pos, end_pos, level=1):
    cost = 0
    mincost = INF_COST
    if cost_elem(elements, end_pos, max_dim) < INF_COST:
        elements[end_pos[0]*max_dim+ end_pos[1]] = 'O'
        visited.add(end_pos)
    else:
        return INF_COST, elements

    if start_pos == end_pos:
        mincost = 0
    elif end_pos in ps:
        mincost = ps[end_pos]
    elif level > max_level:
        mincost = INF_COST
    else:
        up = (end_pos[0], end_pos[1]-1)
        down = (end_pos[0], end_pos[1]+1)
        left = (end_pos[0]-1, end_pos[1])
        right = (end_pos[0]+1, end_pos[1])
        pos_moves = filter(lambda x: cost_elem(elements, x, max_dim) < INF_COST, 
                            [up, down, left,right])
        costs = []
        for move in pos_moves:
            if move not in visited:
                v = copy.copy(visited)
                c, _ = solve_maze(ps, v, elements, max_dim, start_pos, move,
                        level+1)
                costs.append(c + cost_elem(elements, move, max_dim))
        if len(costs):
            cost = min(costs)
        else:
            cost = INF_COST
            visited.remove(end_pos)
        if cost < mincost: 
            mincost = cost
            ps[end_pos] = mincost
    return mincost, elements

def get_locs(within_dist, max_dim, start_pos):
    num_locs = 0
    elements = get_maze(max_dim)
    l = [c for c in xrange(max_dim)]
    coordinates = [c for c in itertools.product(l, repeat=2)]
    pos_storage = {}
    for coord in coordinates:
        cost, _ = solve_maze(pos_storage, set(), elements, max_dim, 
                            start_pos, coord)
        if cost <= within_dist:
            num_locs += 1
            print(num_locs)
            print(coord)
    return num_locs

max_dim = 50
cost, elements = solve_maze(dict(), set(), get_maze(max_dim), max_dim,
        (1,1),(31,39))
print_maze(elements, max_dim)
print(cost)
print(get_locs(50, 50, (1,1)))

