import collections
import itertools
import copy

devices = {} 
devices['A'] = ('polonium', 'g')
devices['B'] = ('thulium', 'g')
devices['C'] = ('promethium', 'g')
devices['D'] = ('ruthenium', 'g')
devices['E'] = ('cobalt', 'g')

devices['F'] = ('polonium', 'm')
devices['G'] = ('thulium', 'm')
devices['H'] = ('promethium', 'm')
devices['I'] = ('ruthenium', 'm')
devices['J'] = ('cobalt', 'm')

NOT_SAFE = 9999999

def eval_cost(diagram):
    isSafe = True
    cost = 1
    for floor in diagram.dg:
        generator_types = []
        for device_code in floor:
            device = devices[device_code]
            if device[1] == 'g': generator_types.append(device[0])
        for device_code in floor:
            device = devices[device_code]
            if device[1] == 'g':
                continue
            if device[1] == 'm' and len(generator_types) == 0:
                continue
            elif device[1] == 'm' and (device[0] in generator_types):
                continue
            else:
                isSafe = False
                cost = NOT_SAFE
                break
        if(not isSafe): break
    return cost

def create_adjacent_positions(diagram, max_floor, min_floor):
    moves = []
    e_pos = diagram.e_pos
    dg = diagram.dg
    for device_1 in dg[e_pos-1]:
        if e_pos + 1 <= max_floor:
            moves.append(make_diagram(dg, [device_1], e_pos, e_pos+1))
        if e_pos - 1  >= min_floor:
            moves.append(make_diagram(dg, [device_1], e_pos, e_pos-1))
    for devices in itertools.combinations(dg[e_pos-1], 2):
        if e_pos + 1 <= max_floor:
            moves.append(make_diagram(dg, devices,e_pos, e_pos+1))
        if e_pos - 1  >= min_floor:
            moves.append(make_diagram(dg, devices, e_pos, e_pos-1))
    return moves

def make_diagram(diagram, devices, before, after):
    dg = copy.deepcopy(diagram)
    for d in devices:
        dg[after-1].append(d)
        dg[after-1].sort()
        dg[before-1].remove(d)
        dg[before-1].sort()
    return Diagram(after, dg)


def solve(pos_storage, lvl_subproblem, start, finish):
    print(len(pos_storage))
    mincost = NOT_SAFE
    if len(finish.dg[-1]) < 5: print(finish)
    if start == finish:
        mincost = 0
    elif (lvl_subproblem, get_diagram_code(finish)) in pos_storage:
        mincost = pos_storage[(lvl_subproblem, get_diagram_code(finish))]
    elif lvl_subproblem <= 0:
        mincost = NOT_SAFE
    else:
        for move in create_adjacent_positions(finish, 4, 1):
            if eval_cost(move) == NOT_SAFE:
                cost = NOT_SAFE
            else:
                cost = solve(pos_storage, lvl_subproblem-1, start, move) + eval_cost(move)
            pos_storage[(lvl_subproblem, get_diagram_code(move))] = cost
            if cost < mincost: 
                mincost = cost
    return mincost

def get_diagram_code(dg):
    s = str(dg.e_pos)
    index = 1
    for floor in dg.dg:
        s+= str(index) + ''.join(floor)
        index += 1
    return s

Diagram = collections.namedtuple('Diagram', ['e_pos', 'dg'])

starting_diagram = Diagram(1,[[c for c in 'ABCDEIJ'],['F', 'H'],[],[]])
finishing_diagram = Diagram(4,[[],[],[],[c for c in 'ABCDEFGHIJ']])
unsafe_diagram = Diagram(2, [[c for c in 'AFGHI'],[],[],[]])
print(eval_cost(starting_diagram))
print(eval_cost(finishing_diagram))
print(eval_cost(unsafe_diagram))
for move in create_adjacent_positions(finishing_diagram, 4, 1):
    print(move)
    print(eval_cost(move))
    print(get_diagram_code(move))

pos_storage = {}
print(solve(pos_storage, 70, starting_diagram, finishing_diagram))
