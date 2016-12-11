import re
def transfer(bots, withTwo, b_num, val):
    if b_num not in bots:
        bots[b_num] = [int(val)]
    else:
        bots[b_num].append(int(val))
        bots[b_num].sort()
        withTwo.append(b_num)

with open('d10input.txt', 'r') as f:
    init_values = []
    bots = {}
    outputs = {}
    withTwo = []
    mv_instructions = []
    for line in f:
        if 'goes to' in line:
            p = line.split()
            b_num = int(p[5])
            val = int(p[1])
            transfer(bots, withTwo, b_num, val)
        else:
            mv_instructions.append(line)
    while(len(mv_instructions) > 0):
        hasFound = False
        for bot in withTwo:
            for i in mv_instructions:
                tok = 'bot ' + str(bot) + ' gives'
                if tok in i:
                    lower = bots[bot][0]
                    higher = bots[bot][1]
                    if lower == 17 and higher == 61:
                        print(bot)
                    lower_bot = int(i.split()[6])
                    higher_bot = int(i.split()[11])
                    if 'output' in i.split()[5]:
                        transfer(outputs, withTwo, lower_bot, lower)
                    else:
                        transfer(bots, withTwo, lower_bot, lower)
                    if 'output' in i.split()[10]:
                        transfer(outputs, withTwo, higher_bot, higher)
                    else:
                        transfer(bots, withTwo, higher_bot, higher)
                    withTwo.remove(bot)
                    bots[bot] = []
                    mv_instructions.remove(i)

    print(outputs)


            
