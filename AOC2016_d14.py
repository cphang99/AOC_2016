import hashlib
import re
import multiprocessing
from itertools import repeat

input_salt = 'zpqevtbw'
test_salt = 'abc'

def h1():
    h = hashlib.md5(input_salt).copy()
    index = 0
    hashesFound = 0
    regexp = re.compile(r'([0-9a-z])\1{2}')
    while(hashesFound < 64):
        h_new = h.copy()
        h_new.update(str(index))
        m = regexp.search(h_new.hexdigest())
        if m is not None:
            c = m.group(0)[0] + '{5}'
            regexp2 = re.compile(c)
            for index2 in xrange(index+1, index+1+1001):
                h_new2 = h.copy()
                h_new2.update(str(index2))
                if regexp2.search(h_new2.hexdigest()) is not None:
                    print(input_salt + str(index))
                    hashesFound += 1
                    break

        index +=1
        
def k_s(hash_dict, index, salt):
    if index in hash_dict:
        return index, hash_dict[index]
    else:
        h_new = hashlib.md5(salt)
        h_new.update(str(index))
        h = h_new.hexdigest()
        for i in xrange(2016):
            h_obj = hashlib.md5(h)
            h = h_obj.hexdigest()
        hash_dict[index] = h
        return index, h

def h3():
    salt = input_salt
    h = hashlib.md5(salt).copy()
    hashesFound = 0
    regexp = re.compile(r'([0-9a-z])\1{2}')
    candidates = {}
    hash_dict = {}
    hexes = map(k_s, repeat(hash_dict,25000), 
            [i for i in xrange(25000)],
            repeat(salt, 25000))
    for h in hexes:
        m = regexp.search(h[1])
        if m is not None:
            candidates[h[0]] = m.group(0)[0] + '{5}'

    index = 0
    while(hashesFound < 64):
        if index in candidates:
            regexp2 = re.compile(candidates[index])
            for index2 in xrange(index+1, index+1+1001):
                _, h = k_s(hash_dict, index2, salt)
                m = regexp2.search(h)
                if m is not None:
                    print(index)
                    hashesFound += 1
                    break
        index += 1
h3()
