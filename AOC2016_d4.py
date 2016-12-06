from operator import itemgetter, attrgetter, methodcaller
sector_id_sum = 0
num_rooms = 0
with open('d4input.txt', 'r') as f:
    for line in f:
        count = {}
        for part in line.split('-')[:-1]:
            for l in part:
                if l not in count:
                    count[l] = 1
                else:
                    count[l] += 1
        toSort = []
        for k, v in count.iteritems():
            toSort.append((k,v))
        toSort.sort(key = itemgetter(0))
        toSort.sort(key= itemgetter(1), reverse=True)
        s = str()
        for i in xrange(5):
            s = s + (toSort[i])[0] 
        cs = line.split('-')[-1].split('[')
        cs_id = cs[0]
        cs_code = cs[1].split(']')[0]
        if s == cs_code:
            sector_id_sum += int(cs_id)
            print(line)
            num_rooms += 1

print(sector_id_sum)
print(num_rooms)


