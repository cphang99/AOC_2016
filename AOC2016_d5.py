import hashlib
import sys

def h1():
    num = 0
    charsFound = 0
    h = hashlib.md5('abbhdwsy').copy()
    while(charsFound < 8):
        h_new = h.copy()
        h_new.update(str(num))
        s = h_new.hexdigest()
        if s.startswith('00000'):
            sys.stdout.write(s[5])
            charsFound += 1
        num += 1
    sys.stdout.write('\n')

def h2():
    num = 0
    charsFound = 0
    pw = {}
    h = hashlib.md5('abbhdwsy').copy()
    while(charsFound < 8):
        h_new = h.copy()
        h_new.update(str(num))
        s = h_new.hexdigest()
        if s.startswith('00000'):
            if (s[5] not in pw) and (int(s[5],16) >= 0) and (int(s[5],16) < 8):
                pw[s[5]] = s[6]
                charsFound += 1
                print(s)
                print('char {0} at pos {1}'.format(s[6], s[5]))
        num += 1
    print(pw)


h2()
