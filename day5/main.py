import utils

vents = []
map = []


def day5(lines):
    maxX = 0
    maxY = 0

    for line in lines:
        [start, end] = utils.str_to_arr(line, ' -> ')
        start = utils.str_to_int_arr(start, ',')
        end = utils.str_to_int_arr(end, ',')

        if start[0] > maxX:
            maxX = start[0]
        if start[1] > maxY:
            maxY = start[1]
        if end[0] > maxX:
            maxX = end[0]
        if end[1] > maxY:
            maxY = end[1]

        vents.append([start, end])

    for _y in range(maxY+1):
        map.append([0] * (maxX+1))

    for vent in vents:
        [start, end] = vent

        if start[0] == end[0] or start[1] == end[1]:
            if start[0] == end[0]:
                x = start[0]
                for y in range(*get_tuple_range([start[1], end[1]])):
                    map[y][x] += 1
                pass
            else:
                y = start[1]
                for x in range(*get_tuple_range([start[0], end[0]])):
                    map[y][x] += 1
                pass
        else:

            steps = max(abs(start[0] - end[0]), abs(start[1] - end[1])) + 1
            x_step = min(max(end[0] - start[0], -1), 1)
            y_step = min(max(end[1] - start[1], -1), 1)

            for step in range(steps):
                x = start[0] + step * x_step
                y = start[1] + step * y_step
                map[y][x] += 1

    print_map()

    print('Count danger zones')
    danger_zone = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] >= 2:
                danger_zone += 1
    print(danger_zone)


def print_map():
    print('Map:')
    for y in range(len(map)):
        print(map[y])


def get_tuple_range(tuple):
    f = tuple[0] if tuple[0] < tuple[1] else tuple[1]
    t = tuple[1] if tuple[0] < tuple[1] else tuple[0]
    return [f, t + 1]
