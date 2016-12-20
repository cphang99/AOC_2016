
INPUT = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'

#INPUT = '.^^.^.^^^^'
FIRST_CHAR = LAST_CHAR = '.'

def eval_char(line, index):
    before = line[index-1] if index-1 >=0 else FIRST_CHAR
    after = line[index+1] if index+1 < len(line) else LAST_CHAR
    if before != after:
        return '^'
    else:
        return '.'

def find_num_safe(line):
    return len([c for c in line if c == '.'])

num_lines = 1
line = INPUT
num_safe = find_num_safe(INPUT)
#print(line)
while(num_lines < 400000):
    next_line = eval_char(line, 0)
    for i in xrange(1,len(line)-1): next_line += eval_char(line, i)
    next_line += eval_char(line, len(line)-1)
    line = next_line
    #print(line)
    num_lines += 1
    num_safe += find_num_safe(line)

print(num_safe)
    
