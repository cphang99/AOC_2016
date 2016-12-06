from operator import itemgetter
with open('d6input.txt', 'r') as f:
    letters = []
    for l in f:
        for c in l:
            if str.isalpha(c):
                letters.append(c)
    print(len(letters))
    index = 0
    for i in xrange(8):
        index = i
        re_lets = {}
        while(index < len(letters)):
            if letters[index] in re_lets:
                re_lets[letters[index]] += 1
            else:
                re_lets[letters[index]] = 1
            index += 8
        re_lets_sorted = []
        for k,v in re_lets.iteritems():
            re_lets_sorted.append((k,v))
        re_lets_sorted.sort(key = itemgetter(1))
        print(re_lets_sorted[0])


