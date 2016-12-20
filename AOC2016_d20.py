ranges = []
with open('d20input.txt', 'r') as f:
    for line in f:
        b_range = line.split('-')
        ranges.append((int(b_range[0]), int(b_range[1])))
    ranges = sorted(ranges)

def find_min_valid(ranges):
    min_valid = 0
    for b_range in ranges:
        print(b_range)
        if min_valid > b_range[1]:
            continue
        elif min_valid >= b_range[0] and min_valid <= b_range[1]:
            min_valid = b_range[1] + 1
            print('min_valid = {0}'.format(min_valid))
        else:
            break
    print(min_valid)


def find_total_valid(ranges):
    total_valid = pow(2,32)
    min_valid = 0
    max_valid = 0
    print('total_valid = {0}'.format(total_valid))
    for b_range in ranges:
        if min_valid > b_range[1] or max_valid > b_range[1]:
            continue
        elif min_valid >= b_range[0] and min_valid <= b_range[1]:
            deducted = b_range[1] - min_valid + 1
            total_valid -= deducted
            min_valid = b_range[1] + 1
            print('min_valid = {0}, total_valid= {1} deducted = {2}'.format(min_valid,
                total_valid, deducted))
        else:
            if max_valid < b_range[0]:
                max_valid = b_range[0]
            deducted = b_range[1] - max_valid + 1
            total_valid -= deducted
            max_valid = b_range[1] + 1
            print('total_valid = {0} deducted = {1} max_valid = {2}'.format(total_valid,
                deducted, max_valid))
        print(b_range)
    print(min_valid)
    print(total_valid)

find_min_valid(ranges)
find_total_valid(ranges)

