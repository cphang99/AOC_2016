def transform(cmd):
    if cmd == 'inc':
        return lambda x: x + 1
    elif cmd == 'dec':
        return lambda x: x - 1
    else:
        raise Exception('UNKNOWN COMMAND {0}'.format(cmd))

with open('d12input.txt','r') as f:
    v = {}
    cmd_lines = [line.split() for line in f]
    counter = 0
    while(counter < len(cmd_lines)):
        cmd = cmd_lines[counter]
        print(cmd)
        print(v)
        if cmd[0] != 'jnz':
            if cmd[0] == 'cpy':
                if cmd[1] in v:
                    v[cmd[2]] = v[cmd[1]]
                else:
                    v[cmd[2]] = int(cmd[1])
            else:
                v[cmd[1]] = transform(cmd[0])(v[cmd[1]])
            counter += 1
        else:
            if cmd[1] in v and v[cmd[1]] != 0:
                counter += int(cmd[2])
            else:
                counter += 1
    print(v['a'])
