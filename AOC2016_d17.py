import collections
import Queue
import hashlib
import re

Node = collections.namedtuple('Node', ['priority', 'cost', 'coordinate', 'visited'])
MAX_X = 3
PASS_CODE = 'pgflpeqp'
GOOD = 1
BAD = 999999
MAX_COST = BAD -1

def get_adj(n):
    x = n.coordinate[0]
    y = n.coordinate[1]
    valid_move = lambda (x,y): True if x >=0 and x <= MAX_X and y>=0 and y <= MAX_X else False
    pos_moves = [m for m in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if
            valid_move(m)]
    return [Node(None, None, c, '') for c in pos_moves]

def eval_cost(n, adj):
    dir_lookup = {'U':0, 'D':1, 'L':2, 'R':3}
    h = hashlib.md5(PASS_CODE + n.visited)
    h_code = h.hexdigest()
    d = get_dir(n, adj)
    cost = GOOD if re.match(r'[bcdef]', h_code[dir_lookup[d]]) else BAD
    return cost

def h(adj, finish):
    x_cost = abs(adj.coordinate[0] - finish.coordinate[0])
    y_cost = abs(adj.coordinate[1] - finish.coordinate[1])
    return x_cost + y_cost

def get_dir(n, adj):
    direction = ''
    n_x = n.coordinate[0]
    adj_x = adj.coordinate[0]
    n_y = n.coordinate[1]
    adj_y = adj.coordinate[1]
    if n_x != adj_x:
        direction = 'L' if adj_x < n_x else 'R'
    elif n_y != adj_y:
        direction = 'U' if adj_y < n_y else 'D'
    return direction
        
#Using modified A* alg
def solve(start, finish):
    open_Q = Queue.PriorityQueue()
    open_Q.put(start)
    while True:
        n = None
        if not open_Q.empty():
            n = open_Q.get()
        else:
            break
        if n.coordinate == finish.coordinate:
            print(n)
            continue
        if n.cost > MAX_COST:
            break
        else:
            for adj in get_adj(n):
                new_cost = n.cost + eval_cost(n, adj)
                if new_cost < BAD:
                    adj = adj._replace(cost = new_cost,
                            priority = new_cost + h(adj,finish),
                            visited = n.visited + get_dir(n, adj))
                    open_Q.put(adj)


start = Node(0, 0, (0,0), '')
finish = Node(0, 0, (3,3), None)
solve(start, finish)

