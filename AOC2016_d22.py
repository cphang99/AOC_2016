import collections
import re

Node = collections.namedtuple('Node', ['coord', 'size', 'used', 'avail',
'percent'])

nodes = []
GOAL = (29, 0)

with open('d22input.txt','r') as f:
    for line in f:
        if not line.startswith('/dev/'):
            continue
        else:
            regexp = re.compile(r'[0-9]+')
            l = line.split()
            coords = l[0].split('-')
            x = int(regexp.search(coords[1]).group(0))
            y = int(regexp.search(coords[2]).group(0))
            s = int(regexp.search(l[1]).group(0))
            u = int(regexp.search(l[2]).group(0))
            a = int(regexp.search(l[3]).group(0))
            p = int(regexp.search(l[4]).group(0))
            nodes.append(Node((x,y), s, u, a, p))

def is_valid(node_pair):
    is_valid = True
    if node_pair[0] == node_pair[1]:
        is_valid = False
    elif node_pair[0].used == 0:
        is_valid = False
    elif node_pair[0].used > node_pair[1].avail:
        is_valid = False
    else:
        is_valid = True

    return is_valid

def print_grid(nodes):
    s = ''
    for i in xrange(30):
        for j in xrange(35):
            if (i, j) == (0,0):
                s += '\''
            elif (i, j) == (0,29):
                s += 'T'
            elif nodes[i*35 + j].used == 0:
                s += '_'
            elif nodes[i*35 + j].used > 200:
                s += '#'
            else:
                s += '.'
        s += '\n'
    return s


valid_nodes = filter(is_valid, [(n1, n2) for n1 in nodes for n2 in nodes])
print(len(valid_nodes))
print(print_grid(nodes))


