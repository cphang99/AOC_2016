import collections
INPUT = 'abcdefgh' 

def find_index(dq, c):
    return [i for i in xrange(len(dq)) if dq[i] == c][0]

cmds = []
with open('d21input.txt', 'r') as f:
    cmds = [l for l in f]

def rev_scramble(cmds):
    index = 0
    for cmd_s in cmds:
        cmd = cmd_s.split()
        if cmd[0] == 'swap' or cmd[0] == 'move':
            p1 = cmd[2]
            p2 = cmd[5]
            cmds[index] = ' '.join(cmd[:2] + [p2] + cmd[3:5] + [p1] + ['\n'])
        elif cmd[0] == 'rotate':
            if cmd[1] == 'based':
                pass
            else:
                if cmd[1] == 'left':
                    c = 'right'
                else:
                    c = 'left'
                cmds[index] = ' '.join([cmd[0]] + [c] + cmd[2:] + ['\n'])
        index += 1
            
    return cmds[::-1]

def process_cmds(input_str, cmds, unscramble=False):
    dq = collections.deque(input_str)
    steps = []
    for line in cmds:
        print(line)
        cmd = line.split()
        if cmd[0] == 'swap':
            if cmd[1] == 'position':
                p1 = dq[int(cmd[2])]
                p2 = dq[int(cmd[5])]
                dq[int(cmd[5])] = p1
                dq[int(cmd[2])] = p2
            else:
                i1 = find_index(dq, cmd[2])
                i2 = find_index(dq, cmd[5])
                dq[i1] = cmd[5]
                dq[i2] = cmd[2]
        elif cmd[0] == 'reverse':
            i1 = int(cmd[2])
            i2 = int(cmd[4])
            rev = [dq[i] for i in xrange(i2, i1-1, -1)]
            for i in xrange(i1,i2+1):
                dq[i] = rev[i-i1]
        elif cmd[0] == 'rotate':
            if cmd[1] == 'based':
                i1 = find_index(dq, cmd[-1])
                if not unscramble:
                    times = 2 + i1 if i1 >=4 else 1 + i1
                    dq.rotate(times)
                else:
                    rot_dict = {0:9, 1:1, 2:6, 3:2, 4:7, 5:3, 6:8, 7:4}
                    dq.rotate(rot_dict[i1] * -1)
            else:
                if cmd[1] == 'left':
                    dq.rotate(int(cmd[2]) * -1)
                else:
                    dq.rotate(int(cmd[2]))
        elif cmd[0] == 'move':
            i1 = int(cmd[2])
            i2 = int(cmd[5])
            c = dq[int(cmd[2])]
            dq.remove(c)
            before = [dq[i] for i in xrange(i2)]
            after = []
            after = [dq[i] for i in xrange(i2, len(dq))]
            dq = collections.deque(before + [c] + after)
        else:
            raise Exception('UKNOWN COMMAND {0}'.format(cmd[0]))
        if len(dq) != len(input_str):
            raise Exception('Input length has changed {0}'.format(''.join(dq)))
        steps.append(line + ''.join(dq))
        print(''.join(dq))
    if unscramble:
        steps.reverse()
    return ''.join(dq), steps

scramble, steps = process_cmds(INPUT, cmds)
print(scramble)
rev_cmds = rev_scramble(cmds)

unscramble, steps = process_cmds(scramble, rev_cmds, True)
print(unscramble)
unscramble2, _ = process_cmds('fbgdceah', rev_cmds, True)
print(unscramble2)
