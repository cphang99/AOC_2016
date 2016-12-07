import re

def m1():
    with open('d7input.txt', 'r') as f:
        numMatches = 0
        for line in f:
            hasMatch = False
            match_indexes = []
            for m in re.finditer(r'(.)\1{1}', line):
                if line[m.start()-1] == line[m.end()]:
                    match_indexes.append((m.start()-1, m.end()))
            for m in re.finditer(r'\[[a-z]+\]', line):
                abba_break = False
                for i in match_indexes:
                    if m.start() < i[0] and m.end() > i[1]:
                        abba_break = True
                        hasMatch = False
                        break
                    else:
                        hasMatch = True
                if(abba_break):
                    break
            if(hasMatch):
                numMatches += 1
                print(line)
        print(numMatches)

def m2():
    with open('d7input.txt', 'r') as f:
        numMatches = 0
        for line in f:
            hasMatch = False
            match_indexes = []
            #Need to use lookaheads to find overlapping examples
            #in order to identify correct answer
            for m in re.finditer(r'(?=(([a-z])(?!\2)[a-z]\2))', line):
                for m2 in re.finditer(r'(?=(([a-z])(?!\2)[a-z]\2))', line):
                    if m.start() != m2.start():
                        if ((line[m.start()] == line[m2.start()+1]) and
                                (line[m.start()+1] == line[m2.start()])):
                            match_indexes.append(((m.start(), m.start()+2),
                                (m2.start(), m2.start()+2)))
            bracket_locs = []
            for m in re.finditer(r'\[[a-z]+\]', line):
                bracket_locs.append( (m.start(), m.end()-1) )
            for i in match_indexes:
                aba_break = False
                bracket_break = False

                #There's two of every paired example, which is why checking
                #only the first that it isn't within a bracket, and then
                #the second that it *is* within a bracket, works.
                for l in bracket_locs:
                    if( ((l[0] > i[0][0]) and (l[0] > i[0][1])) or 
                            ((l[1] < i[0][0]) and (l[1] < i[0][1]))):
                        pass
                    else:
                        bracket_break = True
                        break
                if bracket_break: continue
                for l in bracket_locs:
                    if( ((l[0] < i[1][0]) and l[1] > i[1][1])):
                        aba_break = True
                        hasMatch = True
                        break
                if(aba_break): break

            if(hasMatch):
                numMatches += 1
                print(line)
        print(numMatches)

m2()
