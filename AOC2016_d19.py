import itertools
import collections

NUM_ELVES = 3005290

elves = [e for e in xrange(1,NUM_ELVES+1)]
def s1(elves):
    while(len(elves) > 1):
        e_new = []
        index = 0
        for e in elves:
            if index % 2 == 0:
                e_new.append(e)
                if len(elves)-1 == index:
                    e_new.remove(elves[0])
            index += 1
        elves = e_new
        if len(elves) < 50: print(elves)

    print(e_new)

def s2(elves):
    dq = collections.deque(elves)
    dq.rotate(-(len(dq)//2))
    while(len(dq) > 1):
        dq.popleft()
        if len(dq) % 2 == 0:
            dq.rotate(-1)
    print(dq)

s2(elves)

