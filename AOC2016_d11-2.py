import collections
import itertools
import copy
import multiprocessing

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

devices['K'] = ('elerium', 'g')
devices['L'] = ('elerium', 'm')
devices['M'] = ('dilithium', 'g')
devices['N'] = ('dilithium', 'm')


NOT_SAFE = 9999999
MAX_FLOOR = 4
MIN_FLOOR = 1 

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

def create_adjacent_positions(diagram, max_floor=MAX_FLOOR, min_floor=MIN_FLOOR):
    e_pos = diagram.e_pos
    dg = diagram.dg
    for device_1 in dg[e_pos-1]:
        if e_pos + 1 <= max_floor:
            yield make_diagram(dg, [device_1], e_pos, e_pos+1)
        if e_pos - 1  >= min_floor:
            yield make_diagram(dg, [device_1], e_pos, e_pos-1)
    for devices in itertools.combinations(dg[e_pos-1], 2):
        if e_pos + 1 <= max_floor:
            yield make_diagram(dg, devices,e_pos, e_pos+1)
        if e_pos - 1  >= min_floor:
            yield make_diagram(dg, devices, e_pos, e_pos-1)

def make_diagram(diagram, devices, before, after):
    dg = [f for f in diagram]
    for d in devices:
        dg[after-1] += d
        dg[before-1] = dg[before-1].replace(d, '')
    dg[after-1] = ''.join(sorted(dg[after-1]))
    dg[before-1] = ''.join(sorted(dg[before-1]))
    return Diagram(after, dg)

def solve(start, finish):
    start_visited = {}
    finish_visited = {}
    start_visited[get_diagram_code(start)] = 0
    finish_visited[get_diagram_code(finish)] = 0
    start_moves = [start]
    finish_moves = [finish]
    count = 1
    while(count < 100):
        print('count = {0}'.format(count))
        start_moves = process_nxt_lvl(start_moves, start_visited)
        finish_moves = process_nxt_lvl(finish_moves, finish_visited)
        for mv in start_moves: start_visited[get_diagram_code(mv)] = count 
        for mv in finish_moves: finish_visited[get_diagram_code(mv)] = count
        common = set(start_visited.keys()) & set(finish_visited.keys())
        if common:
            dist = []
            for c in common:
                dist.append(start_visited[c] + finish_visited[c])
            print min(dist)
            break
        count += 1
        print('fwd nodes visited = {0}'.format(len(start_visited)))
        print('bk nodes visited = {0}'.format(len(finish_visited)))
    else:
        print 'no common moves'
        return 'ERROR'
    return 'woohoo'

def process_nxt_lvl(prev_lvl, visited):
    moves = []
    seen_in_lvl = set()
    for dg in prev_lvl:
        for mv in create_adjacent_positions(dg):
            code = get_diagram_code(mv)
            if code not in visited and code not in seen_in_lvl:
                if eval_cost(mv) == 1:
                    moves.append(mv)
                    seen_in_lvl.add(code)
    return moves
        
def get_diagram_code(dg):
    s = str(dg.e_pos)
    index = 1
    for floor in dg.dg:
        s+= str(index) + ''.join(floor)
        index += 1
    return s

Diagram = collections.namedtuple('Diagram', ['e_pos', 'dg'])

starting_diagram = Diagram(1, ('ABCDEGIJKLMN', 'FH', '', ''))
finishing_diagram = Diagram(4, ('', '','', 'ABCDEFGHIJKLMN'))
print(solve(starting_diagram, finishing_diagram))
