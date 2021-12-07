import utils

def day7(lines):
    pos_counts = {}
    pos = sorted(utils.str_to_int_arr(lines[0], ','))
    print(sum(pos))

    for i in range(pos[-1]+1):
        pos_counts[i] = 0
    for i in pos:
        pos_counts[i] += 1

    count = -1
    common = 0
    for i in range(len(pos_counts)):
        if pos_counts[i] > count:
            count = pos_counts[i]
            common = i
    print(common)


    best = -1
    fuel = 99999999999
    for i in range(len(pos)):
        common = i
        _fuel = 0
        for j in range(len(pos)):
            if pos[j] != common:
                for k in range(abs(pos[j] - common)):
                    _fuel += (k + 1)

        if _fuel < fuel:
            fuel = _fuel
            best = common

    print(best)
    print(fuel)
