import itertools

puzzle_input = '10010000000110000'
max_len = 35651584
res = puzzle_input
rev = lambda x: '0' if x == '1' else '1'

def get_slice(arr, range_arr):
    return arr[range_arr[0]: range_arr[1]]

while(len(res) < max_len):
    b = ''.join([rev(x) for x in res[::-1]])
    res += '0' + b

res_forcs = res[:max_len]

checksum = ''
checksum_process = res_forcs
check_complete = False
while not check_complete:
    checksum = ''
    pair_indices = [(c1, c1+2) for c1 in xrange(0, len(checksum_process), 2)]
    pairs = [get_slice(checksum_process, p) for p in pair_indices]
    for pair in pairs:
        checksum += '1' if pair[0] == pair[1] else '0'
    checksum_process = checksum
    check_complete = True if len(checksum) % 2 == 1 else False

print(checksum)



