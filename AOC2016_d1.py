import re
def getDirections(coord, direction):
    path = '+x'
    if coord == 'N' and direction == 'L':
        coord = 'W'
        path = '-x'
    elif coord == 'N' and direction == 'R':
        coord = 'E'
        path = '+x'
    elif coord == 'E' and direction == 'L':
        coord = 'N'
        path = '+y'
    elif coord == 'E' and direction == 'R':
        coord = 'S'
        path = '-y'
    elif coord == 'S' and direction == 'L':
        coord = 'E'
        path = '+x'
    elif coord == 'S' and direction == 'R':
        coord = 'W'
        path = '-x'
    elif coord == 'W' and direction == 'L':
        coord = 'S'
        path = '-y'
    elif coord == 'W' and direction == 'R':
        coord = 'N'
        path = '+y'
    else:
        print("ERROR in processing direction")
        raise Exception
    return coord, path

def processCoord(x, y, path, length, coord_list):
    if path == '+x':
        for i in xrange(0, int(length)):
            coord_list.append((x+i, y))
        x += int(length)
    elif path == '-x':
        for i in xrange(0,int(length)):
            coord_list.append((x-i, y))
        x -= int(length)
    elif path == '+y':
        for i in xrange(0,int(length)):
            coord_list.append((x, y+i))
        y += int(length)
    elif path == '-y':
        for i in xrange(0,int(length)):
            coord_list.append((x, y-i))
        y -= int(length)
    else:
        print("ERROR in processing coordinate")
        raise Exception
    return x, y, coord_list

def main():
    code = """ R2, L5, L4, L5, R4, R1, L4, R5, R3, R1, L1, L1, R4, L4, L1, R4, L4,
    R4, L3, R5, R4, R1, R3, L1, L1, R1, L2, R5, L4, L3, R1, L2, L2, R192, L3,
    R5, R48, R5, L2, R76, R4, R2, R1, L1, L5, L1, R185, L5, L1, R5, L4, R1, R3,
    L4, L3, R1, L5, R4, L4, R4, R5, L3, L1, L2, L4, L3, L4, R2, R2, L3, L5, R2,
    R5, L1, R1, L3, L5, L3, R4, L4, R3, L1, R5, L3, R2, R4, R2, L1, R3, L1, L3,
    L5, R4, R5, R2, R2, L5, L3, L1, L1, L5, L2, L3, R3, R3, L3, L4, L5, R2, L1,
    R1, R3, R4, L2, R1, L1, R3, R3, L4, L2, R5, R5, L1, R4, L5, L5, R1, L5, R4,
    R2, L1, L4, R1, L1, L1, L5, R3, R4, L2, R1, R2, R1, R1, R3, L5, R1, R4 """
    coord = 'N'
    x = 0
    y = 0
    cart_coords = []
    seen = ()
    print(code)
    hasSeen = False
    for full_dir in code.split():
        direction = full_dir[0]
        length = re.match('[0-9]+', full_dir[1:]).group(0)
        coord, path = getDirections(coord, direction)
        x, y, cart_coords = processCoord(x, y, path, length, cart_coords)
        print(x,y)
    print(cart_coords)
    for c in cart_coords:
        if c not in seen:
            s = list(seen)
            s.append(c)
            seen = set(s)
        else:
            if not hasSeen:
                print(c, (x,y))
                hasSeen = True

main()
    



