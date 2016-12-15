import itertools
t = 0

p1 = lambda t: (5 + (t+1)) % 17
p2 = lambda t: (8 + (t+2)) % 19
p3 = lambda t: (1 + (t+3)) % 7
p4 = lambda t: (7 + (t+4)) % 13
p5 = lambda t: (1 + (t+5)) % 5
p6 = lambda t: (t+6) % 3
p7 = lambda t: (t+7) % 11


'''
p1 = lambda t: (4 + (t+1)) % 5
p2 = lambda t: (1 + (t+2)) % 2
'''

for t in itertools.count(0):
    pos = [p1(t), p2(t), p3(t), p4(t), p5(t), p6(t), p7(t)]
    #pos = [p1(t), p2(t)]
    num_passed = filter(lambda x: x == 0, pos)
    if len(num_passed) == len(pos):
        print(t)
        break


