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

starting_diagram = [set()] * 4
starting_diagram[0] = set([devices['A'], devices['B'], devices['G'], devices['C'],
        devices['D'], devices['I'], devices['E'], devices['J']])
starting_diagram[1] = set([devices['F'], devices['H']])
starting_diagram[2] = set()
starting_diagram[3] = set()

finishing_diagram = [set()] * 4
finishing_diagram[0] = set()
finishing_diagram[1] = set()
finishing_diagram[2] = set()
finishing_diagram[3] = {devices['A'], devices['B'], devices['C'], devices['D'],
        devices['E'], devices['F'], devices['G'], devices['H'], devices['I'],
        devices['J']}

class Diagram:
    max_floor = 3
    min_floor = 0
    def __init__(self, diagram, elevator_pos):
        self.diagram = diagram
        self.elevator_pos = elevator_pos - 1

    def __repr__(self):
        s = str()
        index = 1
        for floor in self.diagram:
            s += str(index) + ':'
            for d in floor: s += str(d) + ' '
            s += '\n'
            index += 1
        s += str(self.elevator_pos + 1)
        return s

    def code(self):
        s = str()
        index = 1
        for floor in self.diagram:
            s += str(index)
            f = str()
            for d in floor: f+= devices.keys()[devices.values().index(d)]
            s += ''.join(sorted(f))
            index += 1
        s += str(self.elevator_pos + 1)
        return s

start = Diagram(starting_diagram, 1)
finish = Diagram(finishing_diagram, 4)

class Node:
    node_dict = {}
    def __init__(self, parent, diagram):
        self.parent = parent
        self.diagram = diagram
        self.children = self.create_adjacent_nodes()
        self.cost = self.eval_cost()
        self.code = self.diagram.code()
    def eval_cost(self):
        isSafe = True
        if self.parent is not None:
            cost = self.parent.cost + 1
        else:
            cost = 1
        for floor in self.diagram.diagram:
            generator_types = []
            for device in floor:
                if device[1] == 'g': generator_types.append(device[0])
            for device in floor:
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

    def create_adjacent_nodes(self):
        children = []
        dg = self.diagram.diagram
        pos = self.diagram.elevator_pos
        for device_1 in dg[pos]:
            if self.diagram.elevator_pos + 1 <= Diagram.max_floor:
                children.append(self._move_device([device_1], pos, pos+1)) 
            if self.diagram.elevator_pos -1  >= Diagram.min_floor:
                children.append(self._move_device([device_1], pos, pos-1))
            
            remaining = dg[pos].copy()
            remaining.remove(device_1)
            for device_2 in remaining:
                if self.diagram.elevator_pos + 1 <= Diagram.max_floor:
                    children.append(self._move_device([device_1, device_2],
                        pos, pos+1))
                if self.diagram.elevator_pos -1  >= Diagram.min_floor:
                    children.append(self._move_device([device_1, device_2],
                        pos, pos-1))
        return children

    def _move_device(self, devices, before, after):
        dg = copy.deepcopy(self.diagram)
        if before > after:
            dg.elevator_pos -= 1
        else:
            dg.elevator_pos += 1
        for d in devices:
            dg.diagram[after].add(d)
            dg.diagram[before].remove(d)
        return dg

def solve(node):
    hasFound = False
    Node.node_dict[node.code] = node
    if node.code == finish.code():
        print(n.code)
        print(n.cost)
        hasFound = True
    elif node.cost > 75:
        hasFound = False
    else:
        adj = []
        for dg in node.children: adj.append(Node(node, dg))
        for n in adj:
            if n.code not in Node.node_dict and (n.cost < 50 and
                    len(n.diagram.diagram[3]) < 8):
                if n.cost < 25: print(n.cost) 
                solve(n)
    return hasFound

parent = Node(None, start)
solve(parent)
